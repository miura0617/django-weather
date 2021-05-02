# ���s���@

## (1) git clone����

git clone https://github.com/miura0617/django-weather.git

## (2) ���z�����쐬����

python -m venv venv

## (3) ���z���ɊO�����C�u�������C���X�g�[�����A�J�����𕜌����܂�

pip install -r django-weather\requirements.txt

## (4) �C���X�g�[�������O�����C�u�������m�F

�O�����C�u������django��djangorestframework�����邱�Ƃ��m�F

pip freeze

## (5) manage.py������t�H���_�ړ�����

cd django-weather

## (6) SECRET_KEY���쐬���܂�

�ȉ���URL������weatherproject\get_random_secret_key.py���쐬����SECRET_KEY���쐬���܂�
https://qiita.com/frosty/items/bb5bc1553f452e5bb8ff


python weatherproject\get_random_secret_key.py


## (7) weatherproject\local_settings.py���쐬���A����쐬����SECRET_KEY���`���܂�


## (8) ���f���𐶐�

�ȉ���2�̃R�}���h�����s���A���f���𐶐����܂�

python manage.py makemigrations
python manage.py migrate

## (9) �X�[�p���[�U���쐬

�ȉ��̃R�}���h�ŃX�[�p���[�U���쐬���܂��B

python manage.py createsuperuser


## (10) �T�[�o���N�����܂�

python manage.py runserver


# ����m�F���@

## (1) �Ǘ���ʂɃ��O�C������

�Ǘ���ʁuhttp://127.0.0.1:8000/admin/�v�ɃA�N�Z�X���A�X�[�p�[���[�U�Ń��O�C�����܂�

## (2) ����m�F�̂��߂ɓV�C�����쐬

�Ǘ���ʂ���V�C����2�A3�쐬���܂�

## (3) �V�C���y�[�W�ŕ\�����m�F

�V�C���y�[�W�uhttp://127.0.0.1:8000/top/�v�փA�N�Z�X���A�V�C��񂪕\������邱�Ƃ��m�F���܂��B


## (4) Django Rest Framework�ō쐬����API�T�[�o�̃��X�|���X���m�F

(2)�ō쐬�����V�C����JSON�f�[�^�����X�|���X�Ŏ擾�ł��邱�Ƃ��m�F���܂��B

�uhttp://127.0.0.1:8000/api/1/�v
�uhttp://127.0.0.1:8000/api/2/�v


