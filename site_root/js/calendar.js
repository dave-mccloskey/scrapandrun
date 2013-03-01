goog.require('goog.bind')
goog.require('goog.dom');
goog.require('goog.date');
goog.require('goog.i18n.DateTimeFormat');
goog.require('goog.events');
goog.require('goog.net.XhrIo');
goog.require('goog.json');
goog.require('goog.ui.AdvancedTooltip')

function Calendar(cal, data) {
    this.cal = cal;
    this.data = data;

    this.consts = {
        buttonText: {
            prev: '\u25c0',
            next: '\u25b6',
            prevYear: '&nbsp;&lt;&lt;&nbsp;',
            nextYear: '&nbsp;&gt;&gt;&nbsp;',
            today: 'Today',
        }
    };

    this.go = function() {
        this.date = new goog.date.DateTime();
        this.date.setDate(1); // Set to first of the month
        this.date.setYear(data.year);
        this.date.setMonth(data.month - 1);
        this.monthFormatter = new goog.i18n.DateTimeFormat('MMMM yyyy');
        this.idFormatter = new goog.i18n.DateTimeFormat('yyyy-MM-dd');

        goog.dom.append(this.cal,
            goog.dom.createDom('h2', null,
                goog.dom.createDom('span', {'id': 'headerText'},
                    'Nomonth 2000')));

        /* Setup Next/Prev Month Buttons */
        this.prevButton = goog.dom.createDom('a', null,
            this.consts.buttonText.prev);
        this.nextButton = goog.dom.createDom('a', null,
            this.consts.buttonText.next);
        goog.dom.append(this.cal, goog.dom.createDom('div', {'id': 'changers'},
            [
              this.prevButton,
              this.nextButton
            ]));
        goog.events.listen(this.prevButton, goog.events.EventType.CLICK,
            this.prevMonth, false, this);
        goog.events.listen(this.nextButton, goog.events.EventType.CLICK,
            this.nextMonth, false, this);

        this.table = goog.dom.createTable(6, 7);
        goog.dom.append(this.cal, this.table);
        goog.dom.insertChildAt(this.table,
            goog.dom.createDom('thead', null,
                goog.dom.createDom('tr', null, this.cellsWithDaysOfWeek())),
            0);

        /* Set the initial state */
        history.replaceState(this.makeState());

        this.update();

        window.onpopstate = goog.bind(function(e) {
          if (e.state) {
            this.date.setYear(e.state.year);
            this.date.setMonth(e.state.month);
            this.update();
          }
        }, this);
    };

    this.daysOfWeek = function() {
        return ['S', 'M', 'T', 'W', 'T', 'F', 'S'];
    }

    this.cellsWithDaysOfWeek = function() {
        var days = this.daysOfWeek();
        cells = [];
        for (var i = 0; i < days.length; i++) {
          cells[i] = goog.dom.createDom('th', null, days[i]);
        }
        return cells;
    }

    this.update = function() {
        goog.dom.setTextContent(goog.dom.getElement('headerText'),
            this.monthFormatter.format(this.date));

        var cells = goog.dom.findNodes(this.table, function(node) {
              return node.nodeName == 'TD';
            });

        var d = this.getStartDay();
        for (var i = 0; i < cells.length; i++) {
          var cell = cells[i];
          var id = this.idFormatter.format(d);
          var klass = (d.getMonth() == this.date.getMonth() ?
              "thismonth" : "othermonth");
          goog.dom.removeChildren(cell);
          var wrapper = goog.dom.createDom('div',
              {'class': 'calendarCellWrap'});
          goog.dom.append(cell, wrapper);
          goog.dom.append(wrapper, goog.dom.createDom('div',
              {'id': id, 'class': 'date ' + klass}, '' + d.getDate()));

          d.setDate(d.getDate() + 1)
        }

        // Send request for data for dates
        if (this.request) {
          this.request.abort();
        }
        this.request = new goog.net.XhrIo();
        goog.events.listen(this.request, 'complete', function(){
          //request complete
          if (this.request.isSuccess()) {
            var data = this.request.getResponseJson();
            this.updateDateContents(data);
          }
        }, false, this);
        this.request.send('/clothes/json/calendar/month/' + this.date.getYear()
            + '/' + (this.date.getMonth() + 1) + '/');
    };

    this.getStartDay = function() {
        var dayOfWeek = this.date.getDay();
        var daysToDoInPrevMonth = dayOfWeek;
        var d = new goog.date.DateTime(this.date);
        d.setDate(d.getDate() - daysToDoInPrevMonth);
        return d;
    }

    this.makeState = function() {
      return {
        'year': this.date.getYear(),
        'month': this.date.getMonth()
      };
    };

    this.incrementMonthBy = function(n) {
      this.date.setMonth(this.date.getMonth() + n);
      history.pushState(
          this.makeState(),
          null,
          '/clothes/calendar/' + this.date.getYear()  + '/' +
              (this.date.getMonth() + 1) + '/');
      this.update();
    };

    this.prevMonth = function() {
      this.incrementMonthBy(-1);
    };

    this.nextMonth = function() {
      this.incrementMonthBy(1);
    };

    this.updateDateContents = function(data) {
      var d = new goog.date.DateTime(this.date);
      this.imgReqs = {}
      while (d.getMonth() == this.date.getMonth()) {
        var sDate = this.idFormatter.format(d);
        if (data[sDate]) {
          var div = goog.dom.getElement(sDate);
          var cell = goog.dom.getParentElement(div);

          // Add image
          var img = data[sDate]['img'];
          if (img) {
            this.loadImgAsync(img, cell);
          }

          // Add Tooltip
          this.addToolTip(cell, data[sDate]);
        }

        d.setDate(d.getDate() + 1)
      }
    };

    this.loadImgAsync = function(img, cell) {
      var req = new goog.net.XhrIo();
      goog.events.listen(req, 'complete', function() {
        //request complete
        if (req.isSuccess()) {
          var data = req.getResponseJson();
          this.updateImg(cell, data);
        }
      }, false, this);
      req.send('/clothes/json/photo/320/' + img);
    };

    this.updateImg = function(cell, data) {
      if (data.src) {
        var element = goog.dom.createDom('img', {'src': data.src});
        goog.dom.append(cell, element);
      }
    };

    this.addToolTip = function(element, data) {
      var createTooltipElementHtml = this.createTooltipElementHtml(data);
      var tt = new goog.ui.AdvancedTooltip(element);
      tt.setHtml(createTooltipElementHtml);
      tt.setShowDelayMs(3);
    };

    this.createTooltipElementHtml = function(data) {
      var contents = goog.dom.createDom('div', {'class': 'calendarPopup'});
      var element = goog.dom.createDom('div', {}, contents);
      var ids = data['aoutfit_id'];
      for (var i = 0; i < ids.length; i++) {
        goog.dom.append(contents, goog.dom.createDom(
            'div',
            {'class': 'datecell'},
            goog.dom.createDom(
                'a',
                { 'href': '/clothes/aoutfit/' + ids[i] },
                'A-Outfit: ' + ids[i])));
      }
      return element.innerHTML;
    };
};
