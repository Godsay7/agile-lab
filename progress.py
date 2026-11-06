"""Модуль обчислення прогресу студента в курсі.

User story EDU-7: Як студент, я хочу бачити свій прогрес у курсі,
щоб знати, скільки ще залишилося.
"""

def course_progress(completed_lessons, total_lessons):
    """Повертає відсоток завершених уроків, округлений до цілого.

    completed_lessons - список id пройдених уроків (повтори рахуються один раз)
    total_lessons     - загальна кількість уроків у курсі
    """
    if isinstance(total_lessons, bool) or not isinstance(total_lessons, int):
        raise TypeError("total_lessons має бути цілим числом")
    if total_lessons <= 0:
        raise ValueError("Курс має містити хоча б один урок")

    completed = set(completed_lessons)
    if len(completed) > total_lessons:
        raise ValueError("Пройдених уроків не може бути більше, ніж усього")

    return round(len(completed) * 100 // total_lessons)


def progress_status(percent):
    """Повертає текстовий статус для відображення в інтерфейсі."""
    if not 0 <= percent <= 100:
        raise ValueError("Відсоток має бути в межах 0-100")
    if percent == 0:
        return "Не розпочато"
    if percent == 100:
        return "Завершено"
    return "У процесі"
