# yamdb_final
![example workflow](https://github.com/yasinalizade/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=REST%20API)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/en/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex)](https://cloud.yandex.ru/)

## Description

Project YaMDb collect instances (Review) from users about different products (Titles). Products are divided on several categories: «Books», «Films», «Music». The list of instance (Category) can be updated by the admin (e.g. «Fine arts» or «Jewelry»).
Products by themselves are not represented on YaMDb, you cannot watch film or listen music.
In each category there are works: books, films or music. For example, in the category "Books" there may be works "Sapiens: A Brief History of Humankind" and "I, Robot", and in the category "Music" - the song "Yellow Submarine" by the group "The Beatles" and the second suite of Bach.
A product can be assigned a genre (Genre) from the list of preset ones (e.g. "Fairy Tale", "Rock" or "Arthouse"). New genres can only be created by the admin.
Grateful or indignant users leave text reviews (Review) for the products and rate it in the range from 1 to 10 (an integer); an average rating (integer) of the work is forming by users' ratings. A user can leave only one review per product.

## Aim

This repo was created to develop my skills in CI and CD spheres, please check GitHub Actions to see the deployment process.
