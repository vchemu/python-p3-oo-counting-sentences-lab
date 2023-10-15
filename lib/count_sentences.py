#!/usr/bin/env python3
import re
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
    self._value
    sentences = re.split(r'[.!?]', self._value)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)