import pytest

from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db #usa una base de datos de prueba
def test_get_all_users(api_client):
    user_1 = User.objects.create_user(username='user1', email='u1@test.com')
    user_2 = User.objects.create_user(username='user2', email='u2@test.com', is_active=False)
    url = reverse('users-list')
    response = api_client.get(url) #es lo mismo que haciamos request.get(url)
    result = response.json()
    
    assert response.status_code == 200
    assert result == [
        {
            "username": user_1.username,
            "email": user_1.email,
            "pk": user_1.pk,
            "first_name": "",
            "last_name": "",
            "is_active": True
        },
        {
            "username": user_2.username,
            "email": user_2.email,
            "pk": user_2.pk,
            "first_name": "",
            "last_name": "",
            "is_active": False
        }
    ]


@pytest.mark.django_db
def test_get_all_users_empty_users(api_client):
    url = reverse('users-list')
    response = api_client.get(url)
    result = response.json()

    assert response.status_code == 200
    assert result == []


@pytest.mark.django_db
def test_get_all_users_with_11_user(api_client):
    for x in range(11):
        User.objects.create(
            username=f"user{x}", 
            email=f"u{x}@tests.com"
        )
    url = reverse('users-list')
    response = api_client.get(url)
    result = response.json()

    assert response.status_code == 200
    assert len(result) == 11