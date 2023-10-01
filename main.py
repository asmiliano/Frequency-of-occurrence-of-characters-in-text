def get_character_frequency(text):
  """
  Возвращает словарь с частотой вхождения символов в тексте.

  Args:
    text: Текст, в котором нужно посчитать частоту вхождения символов.

  Returns:
    Словарь с частотой вхождения символов в тексте.
  """

  # Создаем словарь для подсчета символов
  char_dict = {}

  for char in text:
    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1

  return char_dict


def print_character_frequency(char_dict):
  """
  Выводит словарь с частотой вхождения символов в консоль.

  Args:
    char_dict: Словарь с частотой вхождения символов.
  """

  if not char_dict:
    print("Словарь пуст.")
    return

  # Рассчитываем общее количество символов
  total_chars = sum(char_dict.values())

  # Рассчитываем процентное соотношение
  for char in char_dict:
    char_dict[char] = (char_dict[char], char_dict[char] / total_chars * 100)

  # Сортируем по частоте вхождения символов
  sorted_dict = sorted(char_dict.items(), key=lambda item: item[1][0], reverse=True)

  # Выводим результат
  print("Частота вхождения символов в тексте:")
  for char, (count, percent) in sorted_dict:
    print(f"Символ: '{char}', Количество: {count}, Процент: {percent:.2f}%")


if __name__ == "__main__":
  text = """
  A grasshоpper spent the summer hоpping abоut in the sun and singing tо his heart's cоntent. оne day, an ant went hurrying by, lоking very hоt and weary.
  "Why аre you working on such а lovely dаy?" sаid the grаsshopper.
  "I'm collеcting food for thе wintеr," said thе ant, "and I suggеst you do thе samе." And off shе wеnt, hеlping thе othеr ants to carry food to thеir storе. Thе grasshoppеr carriеd on hopping and singing. Whеn wintеr camе thе ground was covеrеd with snow. Thе grasshoppеr had no food and was hungry. So hе wеnt to thе ants and askеd for food.
  "What did yоu dо all summer when we were wоrking tо cоllect оur fооd?" said оne оf the ants.
  "I wаs busy hopping аnd singing," sаid the grаsshopper.
  "Wеll," said thе ant, "if you hop and sing all summеr, and do no work, thеn you must starvе in thе wintеr."
  """

  char_dict = get_character_frequency(text)
  print_character_frequency(char_dict)
