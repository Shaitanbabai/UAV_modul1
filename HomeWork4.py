import logging

logger = logging.getLogger(__name__)


def get_dividend_and_divisor() -> tuple[float, float]:
    while True:
        try:
            print("Введите числитель:")
            dividend = float(input())
            print("Введите знаменатель:")
            divisor = float(input())

            if divisor == 0:
                raise ZeroDivisionError("Деление на ноль!")
            return dividend, divisor
        except (ValueError, ZeroDivisionError) as e:
            logger.error(f"Ошибка: {e}")

            if isinstance(e, ValueError):
                print("Введите числитель и знаменатель как числа!")
            elif isinstance(e, ZeroDivisionError):
                print("Деление на ноль!")

            print("Повторите попытку.")


def divide(dividend: float, divisor: float) -> float:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError(f"Введите числитель и знаменатель как числа!")
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль!")

    result = dividend / divisor
    return result


def main():
    while True:
        try:
            dividend, divisor = get_dividend_and_divisor()
            result = divide(dividend, divisor)
            print(f"Результат деления: {result}")
        except (ValueError, ZeroDivisionError) as e:
            logger.error(f"Ошибка: {e}")
        except Exception as e:
            logger.exception(e)
            print("Произошла непредвиденная ошибка.")
        finally:
            print("Цикл завершен.")


if __name__ == "__main__":
    main()
