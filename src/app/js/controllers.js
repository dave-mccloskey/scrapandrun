angular.module('clothes.controllers', [])
    .controller('Dashboard', function($scope) {
      $scope.articles = [
        {
          'name': 'Foo'
        },
        {
          'name': 'Bar'
        }
      ];
    })
    .controller('MyCtrl2', function($scope) {
      $scope.x = 'test2';
    });
