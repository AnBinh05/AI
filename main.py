# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from  dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def main():
    print('Hello')
information = """
    Gia đình
Gia thế Phan Châu Trinh là một nhà vọng tộc trong huyện. Thân phụ là Phan Văn Bình là một võ quan giữ chức Quản cơ sơn phòng (trông coi công việc ở biên giới vùng núi), hưởng ứng phong trào Cần Vương do Trần Văn Dư và Nguyễn Duy Hiệu lãnh đạo, giữ chức chuyển vận sứ, phụ trách việc quân lương. Mẹ là Lê Thị Trung, con nhà danh tộc làng Phú Lâm (xã Tiên Sơn, huyện Tiên Phước, tỉnh Quảng Nam ngày nay), có đức hiền lành, hiểu biết khá nhiều về văn học Trung Quốc.[1]

Ông Phan Văn Bình xuất thân từ một gia đình giàu có và hào hiệp, quê ở làng Tây Lộc thuộc huyện Hà Đông, sau đổi thành huyện Tiên Phước, phủ Tam Kỳ (nay thuộc xã Tam Lộc, huyện Phú Ninh, tỉnh Quảng Nam). “Ông thân sinh Phan Châu Trinh tên là Bình, học trò trường ba, quyền bá hộ, làm Quản cơ sơn phòng, tán tài kết khách, thanh gươm yên ngựa, có chí muốn lập công danh. Mẹ họ Lê, con nhà danh tộc làng Phú Lâm, có đức hiền lành...”[2]

Vợ chồng ông Phan Văn Bình có 4 người con, 3 người con trai lớn và 1 người con gái út, trong đó Phan Châu Trinh là con thứ ba. Năm 1864, bà Lê Thị Trung mất, ông Bình đi bước nữa và có thêm 2 người con gái. Trong quan hệ họ hàng gia tộc, các anh em nội ngoại của ông Phan Văn Bình đều là những người có tiếng trong vùng về lòng yêu nước, thương dân và đã từng tham gia tích cực các phong trào Nghĩa hội, Duy tân, Đông du... như Lê Cơ, Lê Lượng, Lê Vĩnh Huy, Lê Triêm...[3]

Theo tư liệu từ cuốn “Quảng Nam trong hành trình mở cõi và giữ nước” của Nguyễn Q.Thắng, ông Phan Văn Bình xuất thân từ học trò thi vào trường ba (tú tài), sau đó nhập ngũ vào năm 1884 và giữ chức Quản cơ sơn phòng Dương Yên, dưới quyền chỉ huy của sơn phòng Chánh sứ Trần Văn Dư.

Thời thơ ấu
Phan Châu Trinh sinh ngày 9 tháng 9 năm 1872,[4] người làng Tây Lộc, huyện Tiên Phước, phủ Tam Kỳ (nay thuộc xã Tam Lộc, huyện Phú Ninh), tỉnh Quảng Nam, hiệu là Tây Hồ, Hy Mã, tự là Tử Cán.

Mẹ của Phan Châu Trinh mất sớm vào năm ông lên 6 tuổi. Quê nhà bị quân Pháp đốt cháy trong cuộc trấn áp phong trào Cần vương, nên ông phải theo cha, được cha dạy chữ và dạy võ.

Năm 1886, quân Pháp và quân Nam Triều do Nguyễn Thân chỉ huy tấn công, đánh phá ác liệt các căn cứ hậu bị của nghĩa quân theo phong trào Nghĩa hội ở Trung Lộc, An Lâm, Dương Yên, Đại Đồng, Suối Đá... Sau thời gian cầm cự, lực lượng nghĩa binh dần dần tan rã do chênh lệch về lực lượng và vũ khí thô sơ không tương xứng. Thêm vào đó, lúc này các lãnh tụ ở địa phương có người nghi kỵ lẫn nhau nên không những không còn tin dùng như trước nữa mà còn tìm cách hãm hại nhau.

Riêng đối với Phan Văn Bình, lãnh tụ Nghĩa hội nghi ông là người “có nhị tâm” nên đã cho người sát hại năm 1887 sau các trận đánh ở Nà Lầu, Suối Đá. Theo thân nhân gia đình họ Phan ở Tây Lộc và theo cuốn Phong trào Duy Tân của nhà nghiên cứu Nguyễn Văn Xuân thì ông Phan Văn Bình bị cận vệ của Hường Hiệu chặn bắt tại khu vực cầu Mỹ Lý (nay thuộc xã Tam An, huyện Phú Ninh, tỉnh Quảng Nam) và bị sát hại sau đó vào ngày ngày 15 tháng 6 năm 1886...[3]

Sau khi cha mất,[5] Phan Châu Trinh trở về quê sống với anh là Phan Văn Cừ và tiếp tục đi học. Ông học giỏi, năm 27 tuổi, được tuyển vào trường tỉnh và học chung với Trần Quý Cáp, Huỳnh Thúc Kháng, Nguyễn Đình Hiến, Phan Quang và Phạm Liệu.

Nhà nghiên cứu Nguyễn Q.Thắng cho rằng, chính cái chết oan trái của thân phụ Phan Văn Bình mà sau này chí sĩ Phan Châu Trinh đã có cái nhìn sâu sắc, tường tận về nền quân chủ và dân chủ trong sinh hoạt chính trị - xã hội ở Việt Nam hồi đầu thế kỷ XX.

Sự nghiệp
Khoa Canh Tý (1900), Phan Châu Trinh đỗ cử nhân thứ ba ở trường Thừa Thiên. Năm sau (1901), triều đình mở ân khoa, ông đỗ phó bảng, đồng khoa với tiến sĩ Ngô Đức Kế và phó bảng Nguyễn Sinh Sắc. Khoảng thời gian này, người anh cả mất nên ông về để tang, ở nhà dạy học đến năm Quý Mão (1903) thì được bổ làm Thừa biện Bộ Lễ.

Vào Nam, ra Bắc, sang Nhật
Năm 1905 ông từ quan, rồi cùng với hai bạn học là Trần Quý Cáp và Huỳnh Thúc Kháng (cả hai đều mới đỗ tiến sĩ năm 1904 làm một cuộc Nam du, với mục đích xem xét dân tình, sĩ khí và tìm bạn đồng chí hướng. Đến Bình Định, gặp kỳ khảo hạch thường niên của tỉnh, ba ông lẩn vào các khóa sinh. Vào trường thi, Phan Châu Trinh làm một bài thơ, còn hai bạn thì làm chung một bài phú. Cả ba đều ký tên giả là Đào Mộng Giác. Nội dung bài không theo đầu đề, mà chỉ kêu gọi sĩ tử đang đắm đuối trong khoa trường và danh lợi, hãy tỉnh dậy lo giải phóng giống nòi khỏi cảnh lao khổ.[6][7]

Các tỉnh quan Nam triều hoảng sợ, đem bài trình cho viên Công sứ Pháp, đồng thời ra lệnh truy tìm tác giả, nhưng ba ông đã rời khỏi Bình Định, tiếp tục đi vào các tỉnh phía Nam Trung Kỳ. Trên đường đi, ba ông lần lượt kết giao với Trương Gia Mô, Hồ Tá Bang, Nguyễn Hiệt Chi và hai con trai của danh sĩ Nguyễn Thông là Nguyễn Trọng Lội, Nguyễn Quý Anh.

Sau cuộc Nam du, Phan Châu Trinh ra Nghệ-Tĩnh, Thanh Hóa, Hà Nội để gặp gỡ và hội ý với các sĩ phu tiến bộ, rồi lên căn cứ Đề Thám quan sát tình hình, nhưng ông thấy phong trào này khó có thể tồn tại lâu dài.[8]

Năm 1906 ông bí mật sang Quảng Đông (Trung Quốc) gặp Phan Bội Châu, trao đổi ý kiến rồi cùng sang Nhật Bản, tiếp xúc với nhiều nhà chính trị tại đây (trong số đó có Lương Khải Siêu) và xem xét công cuộc duy tân của xứ sở này.[9] Ông viết:

“	Người nước ta thường tự xưng là đồng loại, đồng đạo, đồng văn với Nhật Bản, thấy họ tiến thì nức nở khen, chứ khi nào chịu xét vì sao họ được tiến như thế? Họ chỉ đóng tàu đúc súng mà được giàu mạnh hay họ còn trau dồi đạo đức, sửa đổi luân lý mới được như ngày nay?
Tôi rất lấy làm lạ cho những người đã qua Nhật về, không đem cái hay cái tốt về cho dân nhờ mà chỉ làm giàu thêm tính nô lệ!

Hay là người mình như kẻ đã hư phổi rồi cho nên một nơi có thanh khí như nước Nhật mà cũng không thở nổi chăng?

Lấy lịch sử mà nói thì dân tộc Việt Nam không phải là không thông minh, thế thì vì lẽ nào ở dưới quyền bảo hộ hơn 60 năm nay mà vẫn còn mê mê muội muội bịt mắt vít tai không chịu xem xét không chịu học hỏi lấy cái hay cái khéo của người.[10]

”
Phát động phong trào
Trong số các sĩ phu đương thời và cả sau này, Phan Châu Trinh là người thấy rõ nhất những nhược điểm của con người và xã hội Việt Nam. Ông chủ trương phải thay đổi từ gốc rễ bằng cách nâng cao trình độ trí tuệ và đạo đức của người Việt, phát triển kinh tế - văn hóa, học những tư tưởng tiến bộ của Phương Tây,ông từ bỏ phong tục tập quán lạc hậu... Ông cho rằng Việt Nam phải phát triển kinh tế và giáo dục để tự lực tự cường, hội nhập vào thế giới văn minh rồi mới nên mưu cầu độc lập chứ không nên cầu viện ngoại bang dùng bạo lực để giành độc lập như chủ trương của Phan Bội Châu. Chỉ như vậy dân tộc Việt Nam mới có nền độc lập chân chính trong quan hệ với ngoại bang còn nhân dân được hưởng tự do trong quan hệ với nhà nước. Phan Châu Trinh viết "Nước ta từ ngày Pháp sang bảo hộ trên mấy mươi năm, người mình học Tây học chỉ làm được việc phiên dịch nói phô mà thôi, không có ai hấp thu được chỗ tinh túy, phăn tìm đến nơi màu nhiệm về mà đào tạo ra học trò để làm việc vẻ vang cho nòi giống. Trái lại, bụng không một hạt gạo mà nói chuyện thi thư, tay không nửa đồng mà tự xưng Khổng Mạnh. Có lẽ da thịt huyết tủy của người nước mình mấy ngàn năm nay đã bị cái hấp lực của huyết dẫn người Tàu chi phối hết cả, nên ngày nay đành làm nộm rối cho người Tàu mà không tự biết chăng? Không thế thì sao lửa đốt bên da mà không biết nóng, sét đánh ngang trán mà không biết sợ, thầy hay bạn giỏi ở một bên mà không biết gắng sức bắt chước bước theo. Thậm chí nữa trằn trọc tráo trở, một hai toan tìm một nước thứ ba nào yêu thương mình mà vui lòng làm tôi làm tớ".[11] Để thực hiện chủ trương của mình, ông đã tổ chức phong trào Duy Tân và viết những bản kiến nghị gửi lên chính quyền thực dân Pháp tại Đông Dương đề nghị họ thực hiện cải cách.

Mùa hè năm 1906 Phan Châu Trinh về nước. Việc làm đầu tiên là gửi một bức chữ Hán (quen gọi là Đầu Pháp chính phủ thư) cho Toàn quyền Paul Beau vạch trần chế độ quân chủ chuyên chế thối nát, yêu cầu nhà cầm quyền Pháp phải thay đổi thái độ đối với sĩ dân nước Việt và sửa đổi chính sách cai trị để giúp người Việt từng bước tiến lên văn minh.

Sau đó, với phương châm "tự lực khai hóa" và tư tưởng dân quyền, Phan Châu Trinh cùng Huỳnh Thúc Kháng, Trần Quý Cáp đi khắp tỉnh Quảng Nam và các tỉnh lân cận để vận động cuộc duy tân. Khẩu hiệu của phong trào lúc bấy giờ là: Khai dân trí, chấn dân khí, hậu dân sinh. Phương thức hoạt động của phong trào là bất bạo động, công khai hoạt động nhằm khai hóa dân tộc, giáo dục ý thức công dân - tinh thần tự do, xây dựng cá nhân độc lập - tự chủ - có trách nhiệm với bản thân và xã hội, thay đổi tận gốc rễ nền văn hóa - tâm lý - tính cách - tư duy - tập quán của người Việt, phổ biến các giá trị của nền văn minh phương Tây như pháp quyền - dân quyền - nhân quyền - dân chủ - tự do - bình đẳng - bác ái, cải cách trên mọi lãnh vực. Phong trào thực hiện mục tiêu cải tạo con người và xã hội Việt Nam bằng cách khuyến khích cải cách giáo dục (bỏ lối học từ chương, xóa mù chữ bằng cách phát động phong trào học Quốc ngữ), mở mang công thương nghiệp, chấn hưng công nghệ, bỏ mê tín dị đoan, thay đổi tập quán (cắt tóc ngắn, cắt ngắn móng tay)...

Thời gian này, ông viết bài Tỉnh quốc hồn ca kêu gọi mọi người duy tân theo hướng khai minh và phát triển thực nghiệp như vừa lược kể.[8]

Hưởng ứng, ở Quảng Nam và các tỉnh lân cận, nhiều trường học, thư xã, thương hội, hội nghề nghiệp,... lần lượt được lập ra.

Tháng 7 năm 1907 Phan Châu Trinh nhận lời mời ra Hà Nội tham gia diễn giảng mỗi tháng 2 kỳ ở Đông Kinh Nghĩa Thục.

Bị giam lần thứ nhất
Tháng 3 năm 1908, phong trào chống sưu thuế Trung Kỳ nổ ra, và bị triều Nguyễn và chính phủ bảo hộ Pháp đàn áp dữ dội. Phan Châu Trinh cùng nhiều thành viên trong phong trào Duy Tân bị nhà cầm quyền buộc tội đã khởi xướng phong trào chống thuế nên đều bị bắt.[12]

Phan Châu Trinh bị bắt ở Hà Nội, giải về Huế. Tòa Khâm sứ Huế và Nam triều đều muốn khép ông vào tội chết. Nhưng nhờ sự can thiệp của những người Pháp có thiện chí và những đại diện của Hội Nhân quyền tại Hà Nội, họ buộc lòng phải kết ông án "trảm giam hậu, lưu tam thiên lý, ngộ xá bất nguyên" (nghĩa là tội chém nhưng chỉ giam lại, đày xa ba ngàn dặm, gặp ân xá cũng không cho về), rồi đày đi Côn Đảo ngày 4 tháng 4 năm 1908.

Nhờ dư luận trong nước và nhờ có sự vận động của Hội Nhân quyền ngay trên đất Pháp, đầu mùa hè năm 1910, Thống đốc Nam Kỳ theo lệnh của Toàn quyền Đông Dương ra Côn Lôn thẩm vấn riêng Phan Châu Trinh. Tháng 8 năm đó ông được đưa về đất liền. Tại Sài Gòn, một hội đồng xử lại bản án cho ông được ân xá, nhưng buộc xuống Mỹ Tho chịu quản thúc. Ở đây, ông làm nhiều bài thơ về các nhân vật tên tuổi của Nam Kỳ.

Bởi không hoạt động gì được, ông viết thư cho Toàn quyền Đông Dương đòi được sang Pháp hoặc trở lại Côn Lôn, nhất định không chịu cảnh bị giam lỏng ở Mỹ Tho nữa. Vì vậy, nhân có nghị định ngày 31 tháng 10 năm 1908 của chính phủ Pháp về việc lập một nhóm giảng dạy tiếng Hán tại Pháp, năm 1911, chính quyền Đông Dương cử một đoàn giáo dục Đông Dương sang Pháp, có cả Phan Châu Trinh và con trai là Phan Châu Dật.

Sang Pháp, bị giam lần thứ hai
Sang Pháp, việc đầu tiên của ông là đưa cho Hội Nhân quyền Pháp bản điều trần về vụ trấn áp những người dân chống sưu thuế tại Trung Kỳ năm 1908 (thường gọi là Trung Kỳ dân biến thủy mạt ký).

Sau đó, ông còn lên tiếng tố cáo tình trạng các tù nhân ở Côn Lôn bị đối xử tồi tệ, và nhờ Liên minh cầm quyền, Đảng Xã hội Pháp can thiệp nhằm giảm án cho các đồng chí của mình. Ông cũng đã tiếp xúc nhiều lần với những nhân vật cao cấp ở Bộ Thuộc địa, với Albert Sarraut (sắp sang nhậm chức Toàn quyền Đông Dương) để đưa ra những dự án cải tổ nền chính trị ở Việt Nam nhưng không có kết quả, vì lúc này thế lực của thực dân hãy còn đang mạnh. Trong khoảng thời gian này, ông viết Pháp-Việt liên hiệp hậu chi Tân Việt Nam.

Ngày 28 tháng 7 năm 1914, Đế quốc Áo-Hung tuyên chiến với Serbia, mở màn cho Chiến tranh thế giới thứ nhất. Sau đó, ngày 3 tháng 8, Đức tuyên chiến với Pháp. Nhân cơ hội này, nhà cầm quyền Pháp tại Paris đã gọi Phan Châu Trinh và Phan Văn Trường (một luật sư, nhà báo người Việt chống thực dân) phải đi lính, nhưng hai ông phản đối với lý do không phải là công dân Pháp.[13] Mấy tháng sau, chính quyền khép tội hai ông là gián điệp của Đức để bắt giam Phan Văn Trường giam ở lao Cherchemidi và Phan Châu Trinh bị giam ở nhà tù Santé (Prison de la Santé), Paris, kể từ tháng 9 năm 1914.

Do việc Phan Châu Trinh bị bắt giam nên trợ cấp giảng dạy của ông bị cắt, con ông mất học bổng, phải vừa học vừa làm. Cũng trong năm này, vợ ông là bà Lê Thị Tỵ qua đời ở quê nhà ngày 12 tháng 5 năm 1914.

Tháng 7 năm 1915, vì không đủ bằng chứng buộc tội, chính quyền Pháp phải trả tự do cho hai ông sau nhiều tháng giam giữ. Sau khi ra tù, Phan Châu Trinh đã soạn tuyển tập thơ Santé thi tập với hơn 200 bài thơ ông sáng tác trong tù.

Ra tù, Phan Châu Trinh học nghề rửa ảnh rồi làm thuê cho các hiệu chụp ảnh để kiếm sống. Trong hoàn cảnh chiến tranh, giá sinh hoạt đắt đỏ, cảnh ngộ của hai cha con rất đỗi cơ cực. Chẳng lâu sau, Phan Châu Dật phải bỏ học về nước vì bị lao ruột và qua đời tại Huế ngày 14 tháng 2 năm 1921, được đem về an táng cạnh mộ mẹ tại Tây Lộc (Tiên Phước, Quảng Nam).[14]

Ngày 19 tháng 6 năm 1919, Phan Châu Trinh cùng với Phan Văn Trường, Nguyễn Thế Truyền và Nguyễn Tất Thành soạn bản "Yêu sách của nhân dân An Nam" gửi cho Hội nghị Versailles, ký tên chung là "Nguyễn Ái Quốc", và đã gây được tiếng vang. Tuy nhiên Phan Châu Trinh không tán thành với con đường đi theo chủ nghĩa cộng sản của Nguyễn Tất Thành. Phan Châu Trinh khuyên Nguyễn Tất Thành không nên ảo tưởng về sự hỗ trợ của người Pháp, kể cả đảng Xã hội Pháp, về vấn đề Việt Nam[15].

Năm 1922, khi vua Khải Định sang Pháp dự đấu xảo Marseille, ông viết một bức thư dài buộc tội vua Khải Định 7 điều, quen gọi là Thất Điều Trần hay Thư Thất Điều, khuyên vua về nước gấp, đừng làm nhục quốc thể. Cũng trong năm này, ông viết bài Tỉnh quốc hồn ca mới. Xuyên suốt tác phẩm này vẫn là một đường lối cải cách dân chủ, vẫn là thực trạng tăm tối của xã hội thực dân phong kiến và những thủ đoạn tàn bạo của chính sách thuộc địa ở Việt Nam.

Thấy hoạt động ở Pháp không thu được kết quả gì, đã nhiều lần ông yêu cầu chính phủ Pháp cho ông trở về quê hương, nhưng đều không được chấp thuận. Mãi đến năm 1925, khi thấy sức khỏe ông đã suy yếu, nhà cầm quyền Pháp mới cho phép ông về nước. Khoảng thời gian này, ông viết cuốn Đông Dương chính trị luận.

Về nước rồi qua đời

Mộ Phan Châu Trinh tại Tân Bình, Thành phố Hồ Chí Minh
Ngày 29 tháng 5 năm 1925, Phan Châu Trinh cùng nhà cách mạng trẻ Nguyễn An Ninh xuống tàu rời nước Pháp, đến ngày 26 tháng 6 cùng năm thì về tới Sài Gòn. Sau đó, ông Ninh đưa ông về thẳng khách sạn Chiêu Nam Lầu[16] của cha mình là ông Nguyễn An Khương. Ở đây mấy ngày thì ông về ở tại nhà riêng của ông Khương ở Mỹ Hòa[17] để tiện việc tiếp đón bạn bè đến thăm và trao đổi công việc, đồng thời cũng để tiện cho ông Nguyễn An Cư (chú của ông Ninh, một lương y nổi tiếng) chăm sóc sức khỏe.

Tuy bị bệnh nhưng Phan Châu Trinh cố gắng diễn thuyết thêm hai đề tài là Đạo đức và luân lý Đông Tây, Quân trị chủ nghĩa và dân trị chủ nghĩa. Hai bài này đã có tác động không nhỏ đến thế hệ trẻ tại Sài Gòn, trong đó có Tạ Thu Thâu. Thân sĩ khắp ba kỳ năng lui tới nơi ở của Phan Châu Trinh, như Trần Huy Liệu và Nguyễn Văn Đính (Bắc Kỳ), Nguyễn Trọng Hy và Huỳnh Phò (Huế), Ngô Châu Danh và Trần Đình Phiên (Hội An), Hồ Tá Bang (Phan Thiết), Bùi Công Trừng (Nam Kỳ)...

Phan Châu Trinh cuối cùng nhận thấy thực dân Pháp không chấp nhận bất cứ một sự cải cách nào có lợi cho nhân dân Việt Nam, tư tưởng của ông có sự thay đổi. Bài “Đạo đức và luân lí Đông Tây” (1925) kết luận: “Nay muốn một ngày kia nước Việt Nam được tự do độc lập thì trước hết dân Việt Nam phải có đoàn thể đã. Mà muốn có đoàn thể thì có chi hay hơn là truyền bá xã hội chủ nghĩa trong dân Việt Nam”[18]

Khi bệnh tình trở nặng (tháng 12 năm 1925), túc trực thường xuyên cạnh Phan Châu Trinh là Nguyễn An Ninh, Phan Văn Trường, Nguyễn Sinh Sắc, Huỳnh Thúc Kháng.

Đang lúc Phan Châu Trinh nằm trên giường bệnh thì hay tin ông Ninh vừa bị mật thám Pháp đến vây bắt tại nhà vào lúc 11 giờ 30 trưa ngày 24 tháng 3 năm 1926. Ngay đêm hôm đó, lúc 21 giờ 30, ông qua đời tại khách sạn Chiêu Nam Lầu và được đem quàn tại Bá Huê lầu, số 54 đường Pellerin, Sài Gòn,[19] hưởng dương 54 tuổi.

Lời trăn trối cuối cùng của Phan Châu Trinh với Huỳnh Thúc Kháng, được thuật lại là:

"Độc lập của dân tộc ta sau này sở cậy có Nguyễn Ái Quốc".[20]
    """
summary_template = """
    cho tôi thông tin {information} về người tôi muốn tìm hiểu :
    1. tóm tắt cuộc đời 
    2. 1 vài điểm nổi  bật 
    """
summary_prompt_temple =PromptTemplate(
input_variables=["information"], template=summary_template
)
# Dùng Gemini thay cho OpenAI/Ollama
#llm = ChatGoogleGenerativeAI(
    #model="gemini-1.5-flash",  # hoặc gemini-1.5-pro
  # temperature=0
#)
llm = ChatOllama(
    model="gemma3:270m",
    temperature=0
)

chain = summary_prompt_temple | llm

response = chain.invoke(input={"information": information})
print(response.content)
