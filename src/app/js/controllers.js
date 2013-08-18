angular.module('clothes.controllers', ['ngResource'])
    .controller('Dashboard', function($scope, $resource) {
      this.Date = $resource('/_/clothes_data/dates', {page_size: 4});
      $scope.dates = this.Date.get();
    })
    .controller('MyCtrl2', function($scope) {
      $scope.x = 'test2';
    });
