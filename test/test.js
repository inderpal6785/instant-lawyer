var request = require('supertest');
request = request('http://google.de');
var assert = require('assert');
describe('whats-app-api', function() {
  describe('/register', function() {
    it('register a numer', function(done) {
      request.get('/register').expect(200, function(err) {
        if (err) done(err);
        else done();
      });
    });
  });
});
