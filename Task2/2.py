"""
Напишите функцию, которая принимает топливо (литры), расход топлива (литры/100 км),пассажиров, кондиционер
(логическое значение) и возвращает максимальное расстояние, которое может проехать автомобиль.
топливо-это количество литров топлива в топливном баке.
Расход топлива-это базовый расход топлива на 100 км (только с водителем внутри).
Каждый дополнительный пассажир увеличивает базовый расход топлива на 5%.
Если кондиционер включен, то его общий (не базовый) расход топлива увеличивается на 10%.

"""
def totalDistance(liters, fuel_consumption: float, passengers: int, conditioner: bool):
    if passengers > 0: #проверяем условие есть ли пассажир в машине, если да то увеличиваем рассход топлива
        fuel_consumption += fuel_consumption * passengers * 5 / 100
    if conditioner: #проверка кондиционера
        fuel_consumption += fuel_consumption * 10 / 100
    distance = liters / fuel_consumption * 100 #итог
    return (round(distance,2))

print(totalDistance(70.0, 7.0, 0, False))
print(totalDistance(36.1, 8.6, 3, True))
print(totalDistance(55.5, 5.5, 5, False))
