angular.module('clothes.controllers', ['ngResource'])
    .controller('Dashboard', function($scope, $resource) {
      this.Date = $resource('/_/clothes_data/dates/', {page_size: 4});
      $scope.dates = this.Date.get();
    })
    .controller('Calendar', function($scope, $resource, $location,
        $routeParams) {
      var yearmonth = $routeParams.yearmonth || moment().format('YYYYMM');
      $scope.date = moment(yearmonth, 'YYYYMM').toDate();

      this.Date = $resource('/_/clothes_data/dates/', {yearmonth: yearmonth});
      var datesWithData = this.Date.get(function() {
        var firstday = moment().startOf('month').startOf('week');
        var lastday = moment().endOf('month').endOf('week');

        // dates is a hash from unix timestamp to { date: foo }
        var dates = {};
        var d = firstday;
        while (d.isBefore(lastday)) {
          dates[d.valueOf()] = {date: d.valueOf()};
          d.add('days', 1);
        }
        // update dates to use value from request if data available
        $.each(datesWithData.results, function(index, date) {
          d = moment(date.date, 'YYYY-MM-DD').valueOf();
          dates[d] = date;
          date['date'] = d;
        });

        // extract values of object into an array
        var dateArray = [];
        $.each(dates, function(key, value) {
          dateArray.push(value);
        });
        $scope.dates = dateArray;

        // array containing week numbers based on number of days
        var weeks = [];
        for (var week = 0; week * 7 < dateArray.length; week++) {
          weeks.push(week);
        }
        $scope.weeks = weeks;
      });
    })
    .filter('week', function() {
      return function(array, week) {
        if (!array) {
          return array;
        }
        var begin = week * 7;
        var end = begin + 7;
        return array.slice(begin, end);
      };
    });
