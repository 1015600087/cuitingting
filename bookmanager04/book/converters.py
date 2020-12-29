# 用于自定义路由转换器
class MobileConverter:
    regex='1[3-9]\d{9}'

    def to_python(self,value):
        return value




