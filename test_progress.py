import pytest

from progress import course_progress, progress_status


# AC1: прогрес показується у відсотках від загальної кількості уроків
def test_progress_half_completed():
    assert course_progress([1, 2, 3, 4, 5], 10) == 50


# AC2: на початку курсу прогрес дорівнює 0%, статус "Не розпочато"
def test_progress_nothing_completed():
    assert course_progress([], 8) == 0
    assert progress_status(0) == "Не розпочато"


# AC3: після проходження всіх уроків прогрес 100%, статус "Завершено"
def test_progress_all_completed():
    assert course_progress([1, 2, 3], 3) == 100
    assert progress_status(100) == "Завершено"


# AC4: повторний перегляд уроку не збільшує прогрес
def test_progress_repeated_lesson_counted_once():
    assert course_progress([1, 1, 2, 2, 2], 4) == 50


# Граничний випадок: дробовий відсоток округлюється до цілого
def test_progress_rounding():
    assert course_progress([1], 3) == 33
    assert course_progress([1, 2], 3) == 67


# Некоректні дані: курс без уроків
def test_progress_zero_total_raises():
    with pytest.raises(ValueError):
        course_progress([], 0)


# Некоректні дані: пройдених більше, ніж усього
def test_progress_more_completed_than_total_raises():
    with pytest.raises(ValueError):
        course_progress([1, 2, 3], 2)


# Некоректні дані: кількість уроків не є цілим числом
def test_progress_wrong_type_raises():
    with pytest.raises(TypeError):
        course_progress([1], "10")


# Статус для проміжного значення та некоректного відсотка
def test_status_in_progress_and_invalid():
    assert progress_status(42) == "У процесі"
    with pytest.raises(ValueError):
        progress_status(120)