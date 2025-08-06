from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):

    def get_boards(self, obj):
        # Importación dentro del método para evitar el ciclo
        from boards.serializers import BoardSerializer

        boards = obj.board_set.all()  # Ajusta según la relación entre User y Board
        return BoardSerializer(boards, many=True, read_only=True).data

    #boards = BoardSerializer(many=True, read_only=True)
    # boards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "boards"]
