from typing import Dict, List
def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:

  # helper function
  def get_probable_words(prefix, keys):
    '''
    Get the possible words when there is a prefix, deal with condition like A.B.prefix or Ord(unfinished keys)
    '''
    probable_words = []
    note = 0
    for key in keys:
      if key.startswith(prefix):
        probable_words.append(key)
        note += 1

    if note == 0:
      return [""]

    return sorted(probable_words)[:5] if len(probable_words) > 5 else sorted(
      probable_words)

  probable_words = {}
  # Convert classes list to a dictionary for easy access
  class_dict = {}
  for cls in classes:
    class_dict.update(cls)


#  For complex condition: for statement with multiple layers like A.B.C...X.Y,
#  we check if the formal chain and layers are correct,
#  and only return the correct possible words only based on the last part of the statement Y.
#  After the processing, the statement we need to process only have length of 2 or 1.
  for statement in statements:
    parts = statement.split('.')
    current_class_name = parts[0]
    temp_class_dict = class_dict
    skip_statement = False
    while len(parts) > 2:
      if current_class_name not in class_dict.keys():
        probable_words[statement] = [""]
        skip_statement = True
        break
      if isinstance(
          class_dict[current_class_name],
          dict) and parts[1] in class_dict[current_class_name].keys():
        temp_class_dict = temp_class_dict[current_class_name]
        parts = parts[1:]
      else:
        probable_words[statement] = [""]
        skip_statement = True
        break
    if skip_statement: continue  #next statement

    # the statement with length 2
    if len(parts) == 2:
      if statement.endswith('.'):  #ends with ., so select all possible words
        class_name = parts[0]
        if class_name in temp_class_dict:
          class_info = temp_class_dict[class_name]
          if isinstance(class_info, dict):
            probable_words[statement] = sorted(
              class_info.keys()) if len(class_info) <= 5 else sorted(
                class_info.keys())[:5]
          elif isinstance(class_info, list):
            # Case 3: Polymorphic type or enum 記得改一下polymorphic。。。
            if class_name in class_info:
              class_info.remove(class_name)  # Remove self from options
            probable_words[statement] = sorted(class_info) if len(
              class_info) <= 5 else sorted(class_info)[:5]

        #   elif isinstance(class_info, str):
        #     probable_words[statement] = [class_info]
          else:
            # Case 2: Empty class
            probable_words[statement] = [""]
      else:
        # Case 4: Partial variable name
        class_name, prefix = parts
        if class_name in temp_class_dict:
          class_info = temp_class_dict[class_name]
          if isinstance(class_info, dict):
            probable_words[statement] = get_probable_words(
              prefix, class_info.keys())
          elif isinstance(class_info, list):
            probable_words[statement] = get_probable_words(prefix, class_info)
          else:
            probable_words[statement] = [""]

    # the statement with length 2
    elif len(parts) == 1:
      class_name = parts[0]
      probable_words[statement] = get_probable_words(class_name,
                                                     temp_class_dict.keys())

  return probable_words
