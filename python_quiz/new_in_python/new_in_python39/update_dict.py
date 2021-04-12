# thêm phương thức update cho dict:
## < python 3.9
old_movies = {
    "Tom": 1,
    "EndGame": 2,
}

new_movies = {
    "Tom": 3,
    "Backup": 123,
}

# < python 3.9 dùng update, và sẽ update lại dict cũ
old_movies.update(new_movies)

## < python 3.9 dùng | thì sẽ tạo được biến movies mới.
movies = new_movies | old_movies
