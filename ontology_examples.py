# this code if for adding information as a fake database



def examples():
    books = [
      {
          "name": "Book1",
          "relations":[
              {
                  "hasISBN":"1231241",
                  "publishedInYear":2002
              }
          ]
      },
        {
          "name": "Book2",
          "relations":[
              {
                  "hasISBN":"212412412",
                  "publishedInYear":2002
              }
          ]
      }, {
          "name": "Book3",
          "relations":[
              {
                  "hasISBN":"12351233",
                  "publishedInYear":2007
              }
          ]
      },
      {
          "name": "Book4",
          "relations":[
              {
                  "hasISBN":"123512354",
                  "publishedInYear":2005
              }
          ]
      }, {
          "name": "Book5",
          "relations":[
              {
                  "hasISBN":"51235231",
                  "publishedInYear":2007
              }
          ]
      },
       {
          "name": "Book6",
          "relations":[
              {
                  "hasISBN":"12351236",
                  "publishedInYear":2007
              }
          ]
      },
       {
          "name": "Book7",
          "relations":[
              {
                  "hasISBN":"7631612341",
                  "publishedInYear":1999
              }
          ]
      },
       {
          "name": "Book8",
          "relations":[
              {
                  "hasISBN":"123512358",
                  "publishedInYear":1998
              }
          ]
      }
  
  ]
  
  authors = [
      {
          "name":'Author1',
          "relations":[{
              "hasName":"Martha Doe",
              "hasNationality":"American"
          }]
      },
        {
          "name":'Author2',
          "relations":[{
              "hasName":"Shhab Georgian",
              "hasNationality":"Egyption"
          }]
      },
        {
          "name":'Author3',
          "relations":[{
              "hasName":"Ali Hasan",
              "hasNationality":"Syrian"
          }]
      },
        {
          "name":'Author4',
          "relations":[{
              "hasName":"Rose Mohammad",
              "hasNationality":"Syrian"
          }]
      }
  ]
  
  
  
  
  
  publisher = [
      {
          "name":'publisher1',
          "relations":[{
              "hasName":"publisher1",
              "hasNationality":"American"
          }]
      },
        {
          "name":'publisher2',
          "relations":[{
              "hasName":"publisher2",
              "hasNationality":"Egyption"
          }]
      },
        {
          "name":'publisher3',
          "relations":[{
              "hasName":"publisher3",
              "hasNationality":"American"
          }]
      },
        {
          "name":'publisher4',
          "relations":[{
              "hasName":"publisher4",
              "hasNationality":"Syrian"
          }]
      }
  ]
  
  
  
  
  
  
  genres = [
      {
          "name":'Genre1',
          "relations":[{
              "label":"Mystery"
          }]
      },
          {
          "name":'Genre2',
          "relations":[{
              "label":"Classic"
          }]
      },  {
          "name":'Genre3',
          "relations":[{
              "label":"action"
          }]
      },
  ]
  
  
 
  
  
  libraries = [
      {
          "name":'Library1',
          "relations":[{
              "label":"Main Library"
          }]
      },
          {
          "name":'Library2',
          "relations":[{
              "label":"Al-Nahawand library"
          }]
      }
  ]
  
  

  
  
  review =  [
      {
          "name":'Review1',
          "relations":[{
              "label":"Great book!",
              "hasReviewValue":5
          }]
      },
          {
          "name":'Review2',
          "relations":[{
              "label":"Very good book!",
              "hasReviewValue":4
          }]
      },  {
          "name":'Review3',
          "relations":[{
              "label":"Good book!",
              "hasReviewValue":3
          }]
      },  {
          "name":'Review4',
          "relations":[{
              "label":"Not so good book!",
              "hasReviewValue":2
          }]
      },
        {
          "name":'Review5',
          "relations":[{
              "label":"bad book!",
              "hasReviewValue":1
          }]
      }
  ]

  return {review,authors,libraries,books,genres}











