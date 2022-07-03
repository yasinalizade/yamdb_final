# yamdb_final

1) [http://84.252.141.212/api/v1]
2) [http://84.252.141.212/admin]
3) [http://84.252.141.212/redoc]

## Description

Project YaMDb collect instances (Review) from users about different products (Titles). Products are divided on several categories: «Books», «Films», «Music». The list of instance (Category) can be updated by the admin (e.g. «Fine arts» or «Jewelry»).
Products by themselves are not represented on YaMDb, you cannot watch film or listen music.
In each category there are works: books, films or music. For example, in the category "Books" there may be works "Sapiens: A Brief History of Humankind" and "I, Robot", and in the category "Music" - the song "Yellow Submarine" by the group "The Beatles" and the second suite of Bach.
A product can be assigned a genre (Genre) from the list of preset ones (e.g. "Fairy Tale", "Rock" or "Arthouse"). New genres can only be created by the admin.
Grateful or indignant users leave text reviews (Review) for the products and rate it in the range from 1 to 10 (an integer); an average rating (integer) of the work is forming by users' ratings. A user can leave only one review per product.

![example workflow](https://github.com/yasinalizade/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)