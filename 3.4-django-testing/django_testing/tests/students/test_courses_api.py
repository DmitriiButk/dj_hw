import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    course = courses_factory()
    response = client.get('/courses/')
    data = response.json()
    assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_get_list_of_courses(client, courses_factory):
    course = courses_factory(_quantity=10)
    response = client.get('/courses/')
    data = response.json()
    for i, course_data in enumerate(data):
        assert course_data['name'] == course[i].name


@pytest.mark.django_db
def test_filter_course_by_id(client, courses_factory):
    course_id = courses_factory(_quantity=3)[0].id
    response = client.get('/courses/')
    data = response.json()
    assert data[0]['id'] == course_id


@pytest.mark.django_db
def test_filter_course_by_name(client, courses_factory):
    course_name = courses_factory(_quantity=3)[0].name
    response = client.get('/courses/')
    data = response.json()
    assert data[0]['name'] == course_name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/courses/', data={'name': 'Test Course'})
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    data = {
        'name': 'Test Course'
    }
    response = client.patch(f'/courses/{course[0].id}/', data=data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.delete(f'/courses/{course[0].id}/')
    assert response.status_code == 204
