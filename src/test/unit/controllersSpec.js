describe('clothes-app clothes.controllers', function() {
  beforeEach(module('clothes.controllers'));

  describe('Calendar', function() {
    var $httpBackend, scope, ctrl;
    beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
      $httpBackend = _$httpBackend_;
      $httpBackend.expectGET('/_/clothes_data/dates?page_size=31&' +
              'yearmonth=201009')
          .respond({results: [
            {
              date: '2010-09-01',
              photo: '2010-09-01.png'
            }
          ]});
      scope = $rootScope.$new();
      ctrl = $controller('Calendar', {
        $scope: scope,
        $routeParams: { yearmonth: '201009' }
      });
      $httpBackend.flush();
    }));

    it('should set date to current date', inject(function() {
      expect(scope.date)
          .toEqual(moment('201009', 'YYYYMM').toDate());
    }));

    it('should set dates to array with all dates on cal', inject(function() {
      // 9/1/10 was a Wednesday.  35 total days
      // more importantly, this should always be a multiple of 7
      expect(scope.dates.length)
          .toEqual(35);
    }));

    it('should set the weeks correctly', inject(function() {
      // 5 weeks for sep 2010
      expect(scope.weeks.length)
          .toEqual(5);
    }));
  });
});
