class Solution:
    def longestPalindrome(self, s: str) -> str:
        if 10 == len(s) or s == s[::-1]  : return s
        rst = ""
        for i,s_t in enumerate(s):
            temp_char = ""
            temp_char += s_t
            for j in range(i,len(s)):
                if i !=j : temp_char += s[j]
                if(temp_char == temp_char[::-1]) :
                    if(len(rst) < len(temp_char)) : rst = temp_char
        return rst

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        #해당 사항 없을 경우 빠르게 처리
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''

        #슬라이딩 윈도우 우측으로
        for i in range(len(s) -1  ):
            result = max(result,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key = len)
        return result
    



s = "babad"
s = "wcqdyulxbzrabuvjjouvlmbzsfpcykmmusxdgrrirljrltlnswqqgyukxjfhzhbpipkswzqroarikxtrlzjriyivdjydlfopqnbqlwiperuaeszhthcunyqejayftrlwiucvlghkurgmnlixfoaokgvucdgzscjkwleifdkjycrgwidibldabhsquotljtvjxitfyrvvwlzxavvgjkmtxswxhutxgeaajuycqpxjraxgsixtmncwauubigsxdjzmgpdwvfztuzsxwyiwjeuzapjmbpfhcdzptmcphjtzdwdlpzzqnomamykbxmsbirtxjqfylatgzzelunzgomohgmlirxkgxregmbhwpoovormmvfrhqoovewpwukfdfxlmqdcvkvjueqrkmsgraexfhdstjaxqxwfbhbuvbnyxckefikkyblrfdrsdgyjckhblycffuqfsrlsenyluxepmscukwruipanugiakyrmmvrcjsgyprrke"
# s = "xiqhechagdpbcdthaafmcnplenylepawbafsmxqlwhzgqmuemwolgoockcafchdsfggulwfzwwkvivnwgbelbbydzfkcfsschvbantskuosunhqihmqjmzgavfnonwhwrkfxgcbowfsebthbrhhklxxyoxiphrgxqodulrbbvdwcclpyjhljgyypztbqzkiyzbfnvnoargyyakaidkiyleurvjbadzwqjtrluayhblhdokmwrwhassruxpftwlbalfvwxtfcqibywsusrlwmbcibvgwnmmdmuhswuperbjoxarhqcpcebbtyhnrouvuwftspmzsmdhfcqovffkuikzrcweffmpnjldoalhcvqvjavllvajvqvchlaodljnpmffewcrzkiukffvoqcfhdmszmpstfwuvuornhytbbecpcqhraxojbrepuwshumdmmnwgvbicbmwlrsuswybiqcftxwvflablwtfpxurssahwrwmkodhlbhyaulrtjqwzdabjvruelyikdiakayygraonvnfbzyikzqbtzpyygjlhjyplccwdvbbrludoqxgrhpixoyxxlkhhrbhtbesfwobcgxfkrwhwnonfvagzmjqmhiqhnusoukstnabvhcssfckfzdybblebgwnvivkwwzfwluggfsdhcfackcooglowmeumqgzhwlqxmsfabwapelynelpncmfaahtdcbpdgahcehqix"
sol = Solution2()
print(sol.longestPalindrome(s))