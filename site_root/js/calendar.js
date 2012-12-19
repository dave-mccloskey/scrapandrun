goog.require('goog.dom');
goog.require('goog.date');
goog.require('goog.i18n.DateTimeFormat');
goog.require('goog.events');

function Calendar(cal) {
    this.cal = cal;
    
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
        this.monthFormatter = new goog.i18n.DateTimeFormat('MMMM yyyy');
        this.idFormatter = new goog.i18n.DateTimeFormat('yyyy-MM-dd');
    
        goog.dom.append(this.cal, 
            goog.dom.createDom('h2', null,
                goog.dom.createDom('span', {'id': 'headerText'}, 'Nomonth 2000')));
        
        /* Setup Next/Prev Month Buttons */
        this.prevButton = goog.dom.createDom('a', null, this.consts.buttonText.prev);
        this.nextButton = goog.dom.createDom('a', null, this.consts.buttonText.next);
        goog.dom.append(this.cal, goog.dom.createDom('div', {'id': 'changers'}, [
            this.prevButton,
            this.nextButton
        ]));
        goog.events.listen(this.prevButton, goog.events.EventType.CLICK, this.prevMonth,
            false, this);
        goog.events.listen(this.nextButton, goog.events.EventType.CLICK, this.nextMonth,
            false, this);
        
        this.table = goog.dom.createTable(6, 7);
        goog.dom.append(this.cal, this.table);
        goog.dom.insertChildAt(this.table,
            goog.dom.createDom('thead', null,
                goog.dom.createDom('tr', null, this.cellsWithDaysOfWeek())),
            0);
        
        this.update();
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
        
        var cells = goog.dom.findNodes(this.table, function(node) { return node.nodeName == 'TD'; });
        
        var d = this.getStartDay();
        for (var i = 0; i < cells.length; i++) {
          var cell = cells[i];
          var id = this.idFormatter.format(d);
          var klass = (d.getMonth() == this.date.getMonth() ? "thismonth" : "othermonth");
          goog.dom.removeChildren(cell);
          goog.dom.append(cell, goog.dom.createDom('div', {'id': id, 'class': 'date ' + klass}, '' + d.getDate()));
          
          d.setDate(d.getDate() + 1)
        }
    };
    
    this.getStartDay = function() {
        var dayOfWeek = this.date.getDay();
        var daysToDoInPrevMonth = dayOfWeek;
        var d = new goog.date.DateTime(this.date);
        d.setDate(d.getDate() - daysToDoInPrevMonth);
        return d;
    }
    
    this.incrementMonthBy = function(n) {
      this.date.setMonth(this.date.getMonth() + n);
      this.update();
    }
    
    this.prevMonth = function() {
      this.incrementMonthBy(-1);
    }
    
    this.nextMonth = function() {
      this.incrementMonthBy(1);
    }
    
};

