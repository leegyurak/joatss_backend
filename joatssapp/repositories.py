from joatssapp.models import Traffic


class JoatssRepository:
    def create_traffic(self, ip: str) -> Traffic:
        return Traffic.objects.create(ip=ip)
