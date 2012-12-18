goog.require('goog.dom');
goog.require('goog.date');
goog.require('goog.i18n.DateTimeFormat');

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
        this.formatter = new goog.i18n.DateTimeFormat('MMMM yyyy');
    
        goog.dom.append(this.cal, 
            goog.dom.createDom('h2', null,
                goog.dom.createDom('span', {'id': 'headerText'}, 'Nomonth 2000')));
        
        goog.dom.append(this.cal, goog.dom.createDom('div', {'id': 'changers'}, [
            goog.dom.createDom('button', null, this.consts.buttonText.prev),
            goog.dom.createDom('button', null, this.consts.buttonText.next)
        ]));
        
        this.table = goog.dom.createTable(6, 7);
        goog.dom.append(this.cal, this.table);
        
        this.update();
    };
    
    this.update = function() {
        goog.dom.setTextContent(goog.dom.getElement('headerText'),
            this.formatter.format(this.date));
    };
};

