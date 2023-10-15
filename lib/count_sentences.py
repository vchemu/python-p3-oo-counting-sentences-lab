#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self._value
  
  def set_value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    value = self.value
    for mark in ["!", "?", ","]:
      value = value.replace(mark, ".")
    all_sentences = [x for x in value.split(".") if x]
    return len(all_sentences)