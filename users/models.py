import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class GerenteManager(BaseUserManager):
    def create_user(self, nome_completo, cpf, email, password=None):
        if not email:
            raise ValueError('O endereço de email é obrigatório')
        if not cpf:
            raise ValueError('O CPF é obrigatório')

        email = self.normalize_email(email)  # Normalização do email
        user = self.model(
            nome_completo=nome_completo,
            cpf=cpf,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome_completo, cpf, email, password=None):
        user = self.create_user(
            nome_completo=nome_completo,
            cpf=cpf,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Gerente(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = GerenteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'cpf']

    class Meta:
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

    def __str__(self):
        return self.nome_completo

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
