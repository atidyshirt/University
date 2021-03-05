// Using: https://www.json-generator.com/

[
  '{{repeat(105)}}',
  {
    firstName: '{{firstName()}}',
    lastName: '{{surname()}}',
    email: '{{email()}}',
    dateOfBirth: '{{date(new Date(1900, 0, 1), new Date(2007, 0, 1) , "YYYY-MM-dd")}}',
    homeAddress: '{{integer(1, 999)}} {{street()}}, {{city()}}',
    
    id: '{{index()}}',
    
    nickname: '{{firstName()}}',
    middleName: '{{firstName()}}',
    bio: '{{lorem(1, "paragraphs")}}',
    created: '{{date(new Date(2021, 1, 24), new Date(), "ISODateTime")}}',
    role: function(tags) {
      if (tags.index() === 0) return "defaultGlobalApplicationAdmin";
      if (Math.random() < 0.03) return "globalApplicationAdmin";
      return "user";
    },
    phone: function(tags) {
      var num = Math.random() < 0.5? tags.phone("x xxx xxxx"): (tags.random("21", "22", "27") + " " + tags.phone("xxx xxxx")); // landline/mobile
      num = (Math.random() < 0.5? "+64 ": "0") + num; // country code/domestic
      return num;
    },
    businessesAdministered: ['{{repeat(0, 10)}}', '{{integer()}}']
  }
]