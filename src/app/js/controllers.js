angular.module('clothes.controllers', ['ngResource'])
    .controller('Dashboard', function($scope, $resource) {
      this.Article = $resource('/_/clothes_data/articles');
      $scope.articles = this.Article.get();
    })
    .controller('MyCtrl2', function($scope) {
      $scope.x = 'test2';
    });
