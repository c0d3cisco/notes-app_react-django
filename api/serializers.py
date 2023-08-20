from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer): # - one per class/model
  class Meta:
    model = Note
    fields = '__all__'
    # fields = ['body', 'updated'] # - fields we want to serialize