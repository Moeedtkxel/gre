from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from .models import Questions_detail, Options, Questions


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('optionA', 'optionB', 'optionC',
                  'optionD', 'optionE', 'optionF',
                  'optionG', 'optionH', 'optionI',)

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                    # Do not serialize empty lists
                    continue
                ret[field.field_name] = represenation

        return ret


#
class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=False, read_only=True)

    class Meta:
        model = Questions
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    question_type = serializers.CharField(source="question.question_type", read_only=True)
    question = QuestionSerializer(many=False, read_only=True)

    class Meta:
        model = Questions_detail
        fields = ('question_type', 'question', 'difficulty_level')
        read_only_fields = ('question_type',)
        # depth = 2

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                    # Do not serialize empty lists
                    continue
                if isinstance(represenation, dict):
                    if represenation['options']:
                        if represenation['question_type'] in [1, 4, 5]:
                            options = represenation['options']
                            listofdicts = []
                            dict1 = dict((k, options[k]) for k in ('optionA', 'optionB', 'optionC',
                                                                   'optionD', 'optionE', 'optionF',
                                                                   'optionG', 'optionH', 'optionI') if k in options)

                            listofdicts.append(dict1)
                            represenation['options'] = listofdicts
                        if represenation['question_type'] == 2:
                            options = represenation['options']
                            listofdicts = []
                            dict1 = dict((k, options[k]) for k in ('optionA', 'optionB', 'optionC') if k in options)
                            dict2 = dict((k, options[k]) for k in ('optionD', 'optionE', 'optionF') if k in options)
                            listofdicts.append(dict1)
                            listofdicts.append(dict2)
                            represenation['options'] = listofdicts
                        if represenation['question_type'] == 3:
                            options = represenation['options']
                            listofdicts = []
                            dict1 = dict((k, options[k]) for k in ('optionA', 'optionB', 'optionC') if k in options)
                            dict2 = dict((k, options[k]) for k in ('optionD', 'optionE', 'optionF') if k in options)
                            dict3 = dict((k, options[k]) for k in ('optionG', 'optionH', 'optionI') if k in options)
                            listofdicts.append(dict1)
                            listofdicts.append(dict2)
                            listofdicts.append(dict3)
                            represenation['options'] = listofdicts
                ret[field.field_name] = represenation

        return ret
