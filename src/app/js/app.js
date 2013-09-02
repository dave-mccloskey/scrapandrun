angular.module('clothes', ['clothes.controllers',
          'clothes.filters',
          'clothes.services',
          'link'
    ])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/dashboard',
            {templateUrl: 'partials/dashboard.html', controller: 'Dashboard'});
        $routeProvider.when('/calendar',
            {templateUrl: 'partials/calendar.html', controller: 'Calendar'});
        $routeProvider.otherwise({redirectTo: '/dashboard'});
      }]);
