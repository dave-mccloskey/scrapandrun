angular.module('clothes.controllers', [])
    .controller('MyCtrl1', function($scope) {
      $scope.x = 'test1';
    })
    .controller('MyCtrl2', function($scope) {
      $scope.x = 'test2';
    });
