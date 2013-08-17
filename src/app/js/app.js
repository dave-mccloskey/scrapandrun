angular.module('clothes', ['clothes.controllers',
          'clothes.filters',
          'clothes.services'
    ])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/dashboard',
            {templateUrl: 'partials/dashboard.html', controller: 'Dashboard'});
        $routeProvider.when('/view2',
            {templateUrl: 'partials/partial2.html', controller: 'MyCtrl2'});
        $routeProvider.otherwise({redirectTo: '/dashboard'});
      }]);
