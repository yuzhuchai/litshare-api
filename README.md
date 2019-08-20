LitShare API

_____________________________________________________________________________________________________________

END POINTS:

GET /users/login    >>>>>>>> GET user login                                             
POST /users/register  >>>>>>>> POST user register for new account                               
GET /users/id         >>>>>> GET user show page, includes borrow history                          
DELETE /users/id 	>> close account                                                         
GET /users/logout   >>>>> user log out                                                  
PUT /users/id/edit    >>>>>>> edit user                                                  
		

GET /books   >>>>>> homepage showing 3 random books                                                  
GET /books/id    >>>>>>>> get individual book info (including book info copies?)                             
POST /books   >>>>>>> create book                                                    
GET /books/book_id/copy   	>>>>>>>>>> all the copies, with locations, and usernames attached                          
GET /books/book_id/copy/copy_id     >>>>>>> individual copy or                                                
DELETE /books/book_id/copy/copy_id   >>>>>>>> delete individual copy                                                  
POST /books/book_id/copy   >>>>>>>>  create copy of a book to lend                                               
PUT /books/book_id/copy/copy_id     >>>>>>>> update copy                                               


POST /requests    >>>>>>>>>>>>Create request                                                
GET /requests/request_id    >>>>>>>>>>>> Get one single request                                               
GET /requests/sent/user_id    >>>>>>>>>> Get requests that a user sent                                                
GET /requests/received/user_id   >>>>>>>>>>> Get requests a user receives                                                
PUT /requests/request_id >>>>>>> deny request or Approve request, if approved create loan                                  
PUT /loan/loan_id   >>>>>>>>> return book, update loan                                                

_____________________________________________________________________________________________________________
