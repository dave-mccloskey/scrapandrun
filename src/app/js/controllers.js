'use strict';

/* Controllers */

function MyCtrl1($scope) {
  $scope.x = 'test1';
};
MyCtrl1.$inject = ['$scope'];

function MyCtrl2($scope) {
  $scope.x = 'test2';
};
MyCtrl2.$inject = ['$scope'];

angular.module('clothes.controllers', [])
  .controller('MyCtrl1', [MyCtrl1])
  .controller('MyCtrl2', [MyCtrl2]);
