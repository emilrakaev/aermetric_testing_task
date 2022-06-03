from rest_framework import serializers


class AircraftStatDataSerializer(serializers.Serializer):
    type = serializers.CharField(required=False, allow_null=True)
    aircraft = serializers.CharField(required=False, allow_null=True)
    status = serializers.CharField(required=False, allow_null=True)
    errors_count = serializers.IntegerField()
    info_count = serializers.IntegerField()
    lower_a = serializers.IntegerField()
    lower_b = serializers.IntegerField()
    paired_a = serializers.IntegerField()
    paired_b = serializers.IntegerField()
    upper_a = serializers.IntegerField()
    preLegend = serializers.IntegerField()
    legend = serializers.IntegerField()
    repeat_legend = serializers.IntegerField()
    warning = serializers.IntegerField()

    class Meta:
        fields = ('type', 'aircraft', 'status', 'errors_count', 'info_count', 'lower_a', 'lower_b', 'paired_a',
                  'paired_b', 'upper_a', 'preLegend', 'legend', 'repeat_legend', 'warning')


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField(required=False)
