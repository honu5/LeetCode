class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        far=celsius*1.80+32.00
        kel=celsius+273.15
        return [kel,far]
        