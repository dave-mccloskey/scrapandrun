'use strict';

var appModule = angular.module('clothes',
    [
      'clothes.controllers',
      'clothes.filters',
      'clothes.services'
    ]);
// Declare app level module which depends on filters, and services
appModule.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1',
        {templateUrl: 'partials/partial1.html', controller: MyCtrl1});
    $routeProvider.when('/view2',
        {templateUrl: 'partials/partial2.html', controller: MyCtrl2});
    $routeProvider.otherwise({redirectTo: '/view1'});
  }]);
