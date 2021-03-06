angular.module('link', [])
    .directive('activeLink', ['$location', function(location) {
      return {
        restrict: 'A',
        link: function(scope, element, attrs, controller) {
          var clazz = attrs.activeLink;
          var path = $(element).children("a")[0].hash.substring(1);
          scope.location = location;
          scope.$watch('location.path()', function(newPath) {
            if (path === newPath) {
              element.addClass(clazz);
            } else {
              element.removeClass(clazz);
            }
          });
        }
      };
    }]);
