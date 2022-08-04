from tkinter import VERTICAL
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="Project Kelompok 8", layout="wide")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Information'], 
        icons=['house', 'info-square'], menu_icon="cast", default_index=1)
    selected

# CSS style definitions
selected2 = option_menu(None, ["Get to know about cybersecurity", "Phising",  "10 Cara untuk menghindari phising"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="vertical",
    styles={
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "#262730", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#FAFAFA"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    }
)

if selected == "Home": 
    if selected2 =="Get to know about cybersecurity":
        st.title('Get to know about cybersecurity')
        tab1, tab2, tab3 = st.tabs(["Apa itu cybersecurity?", "3 Jenis ancaman cybersecurity", "10 metode ancaman cybersecurity"])
        with st.container():    

            with tab1:
                st.header('Apa Itu Cybersecurity?')
                st.image("cao.jpg", width=750)
                st.write('Dilansir dari CISCO, cybersecurity adalah proses perlindungan sistem, data, jaringan, dan program dari ancaman atau serangan digital. Biasanya, serangan ini dilakukan oleh pihak tak bertanggung jawab untuk berbagai macam hal. Beberapa contohnya adalah mengakses informasi sensitif, atau bahkan mengubah dan menghancurkan data penting. Motifnya bisa jadi untuk mengganggu sebuah bisnis, atau bisa juga untuk memeras uang dalam jumlah yang biasanya tidak sedikit. Banyak orang yang menganggap bahwa cybersecurity sama dengan information security (biasa disebut InfoSec). Padahal dua hal ini adalah sesuatu yang berbeda. InfoSec adalah elemen penting dari cybersecurity, khusus untuk menangani keamanan data. Cybersecurity bisa dikatakan sebagai payung besar dari InfoSec dan elemen lainnya.')
    
            with tab2:
                st.header('3 Jenis Ancaman Cyber Security')
    #diganti jadi st.writer
                st.write("Bersamaan dengan perkembangan teknologi yang semakin pesat, jenis dan metode ancaman cyber security pun semakin bertambah setiap harinya. Nah berikut ini adalah 3 jenis ancaman cyber security populer yang mungkin Anda temui pada sistem, jaringan, atau aplikasi Anda.")  
                st.subheader("1. Cyber Crime")
    #diganti jadi st.writer
                st.write("Singkatnya, cybercrime adalah kejahatan siber yang menargetkan sebuah sistem dan jaringan komputer. Disini komputer digunakan sebagai alat dan juga target dari kejahatan tersebut. Cyber crime terjadi saat hacker menggunakan sebuah perangkat untuk mengakses dan mencuri informasi pribadi, bisnis, maupun pemerintah untuk keperluan pribadi. Umumnya, informasi dan data yang didapatkan melalui kejahatan cyber crime ini akan dijual secara online atau disalahgunakan oleh pihak yang tidak bertanggung jawab.")
                st.subheader("2. Cyber Attack")
    #diganti jadi st.writer
                st.write("Pada dasarnya, cyber attack adalah bagian dari cyber crime atau kejahatan siber. Bedanya, cyber attack umumnya melibatkan kepentingan politik dan organisasi. Kejahatan cyber attack dilakukan untuk mengumpulkan informasi rahasia sebuah organisasi, mendapatkan dan mencuri data sensitif, hingga mengambil alih sistem.")
                st.subheader("3. Cyber Terrorism")
    #diganti jadi st.writer
                st.write("Sama seperti cyber attack, kejahatan cyber terrorism menargetkan organisasi politik melalui terror seperti ancaman, provokasi, dan intimidasi online. Cyber terrorism umumnya dilakukan untuk menimbulkan kepanikan dan ketakutan skala besar agar hacker bisa mendapatkan apa yang mereka inginkan. Bentuk kejahatan cyber terrorism pun beragam. Mulai dari pencurian data, pengambilan alih sistem, serangan malware, penghapusan data, dan lain sebagainya")
    
            with tab3:
                st.header("10 Metode Ancaman Cyber Security")
                st.write("Berikut ini adalah 10 metode ancaman cyber security yang mungkin Anda temui sehari-hari!")
                st.subheader("1. Malware")
                st.write("Salah satu metode ancaman cyber security paling umum saat ini adalah serangan malware (malicious software) atau perangkat lunak berbahaya. Singkatnya, malware adalah sebuah program yang didesain secara khusus oleh para hackers untuk mengeksploitasi dan merusak perangkat, server, maupun jaringan Anda.")
                st.subheader("2. Ransomware")
                st.write("Pada dasarnya, ransomware adalah salah satu tipe serangan malware yang paling berbahaya. Perangkat lunak yang satu ini mempunyai kemampuan merusak dan mengunci data. Tidak hanya itu, Ransomware ini juga bisa melumpuhkan perangkat Anda secara keseluruhan, sehingga Anda sama sekali tidak bisa mengakses dan menggunakan device tersebut.")
                st.subheader("3. Brute force attack")
                st.write("Secara sederhana, brute force attack adalah upaya hacker untuk mengakses sebuah sistem dan jaringan secara paksa melalui tebakan username dan password. Dalam melancarkan serangannya, pelaku menggunakan metode trial-and-error dengan mencoba ribuan kombinasi kata sandi agar bisa melewati proses autentikasi sistem. Sebenarnya, brute force adalah metode ancaman cyber security yang cukup outdated. Namun,  jenis cybercrime ini mempunyai success rate yang cukup tinggi dan dinilai sangat efektif.")
                st.subheader("4. Spoofing")
                st.write("Jika Anda pernah mendapatkan telepon dan pesan mengaku sebagai teman atau kerabat yang meminta bantuan finansial? Nah, inilah yang dinamakan spoofing. Singkatnya, spoofing adalah tindakan hackers yang berpura-pura menjadi orang yang Anda kenal untuk melakukan berbagai tindakan kriminal. Metode ancaman cyber security yang satu ini memang tidak sama dengan ancaman siber yang lainnya. Namun, ancaman yang dibawa pun tetap berbahaya. Spoofing juga bisa menyasar jaringan maupun server. Attacker nantinya akan mengelabui jaringan/server Anda dengan menggunakan identitas palsu. Menggunakan alamat IP address palsu hingga dianggap sebagai sumber yang terpercaya dan mendapatkan akses ke dalam jaringan/server, contohnya.")
                st.subheader("5. Social engineering")
                st.write("Dilansir dari Imperva, social engineering adalah istilah yang digunakan untuk menggambarkan serangan yang didasarkan oleh interaksi manusia. Singkatnya, social engineering memanipulasi pengguna untuk memberikan informasi sensitif seperti password, jawaban untuk pertanyaan keamanan, dan lainnya. Biasanya, jenis ancaman ini memanfaatkan rasa ingin tahu manusia dan memancingnya untuk melakukan hal-hal yang mungkin terasa biasa saja, tetapi sebenarnya membahayakan.")
                st.subheader("6. Phishing")
                st.write("Ancaman cybersecurity yang terakhir adalah phishing. Phishing merupakan bentuk penipuan yang biasanya hadir melalui email. Penipu akan mengirimkan email menggunakan alamat yang mirip dengan sumber terpercaya. Meskipun begitu, terdapat satu atau dua huruf berbeda yang biasanya tidak terlihat secara kasat mata. Penipuan ini bertujuan untuk mencuri data sensitif seperti nomor keamanan kartu kredit (CVC), password, dan informasi penting lainnya. Jadi, jika mendapatkan email yang mewajibkan kamu untuk memasukkan data sensitif, selalu pastikan kembali kredibilitas pengirim email tersebut.")
                st.subheader("7. DoS (Denial of Service") 
                st.write("Denial of service (DoS) adalah jenis serangan cyber yang menyerang komputer atau jaringan sehingga tidak dapat menanggapi permintaan. ")
                st.subheader("8. Man in the Middle (MITM)")
                st.write("MITM terjadi ketika peretas sudah memasukkan diri ke dalam transaksi dua pihak. Setelah mengganggu lalu lintas, mereka bisa menyaring dan mencuri data. Serangan jenis ini sering terjadi ketika pengguna internet sedang terhubung ke internet dengan jaringan WiFi publik yang tidak aman. Hacker akan memanfaatkan situasi ini dengan menyisipkan diri di antara para pengguna dan jaringan. Mereka kemudian menggunakan malware untuk menginstal perangkat lunak dan menggunakan data secara ilegal.")
                st.header("9. Injeksi SQL")
                st.write("Injeksi Structured Query Language (SQL) merupakan jenis serangan cyber yang dilakukan dengan memasukkan kode berbahaya ke dalam server yang menggunakan SQL. Saat terinfeksi, server akan merilis informasi yang bisa disalahgunakan oleh peretas. ") 
                st.subheader("10. Serangan Kata Sandi")
                st.write("Dengan memasukkan kata sandi yang tepat, penyerang cyber bisa memiliki akses ke banyak informasi. Rekayasa sosial adalah jenis serangan kata sandi yang oleh Data Insider disebut sebagai strategi cyber security attack yang memanfaatkan interaksi manusia untuk melanggar praktik keamanan standar. Serangan kata sandi lainnya juga bisa dilakukan dengan mengakses basis data kata sandi atau dengan menebak-nebak kata sandi orang.")
    
    if selected2==("Phising"):
        st.title("Phising")
        st.header("Apa itu phising?")
        st.write("Serangan phishing adalah komunikasi palsu yang tampaknya berasal dari sumber yang dapat dipercaya tetapi dapat membahayakan semua jenis sumber data. Serangan dapat memfasilitasi akses ke akun online dan data pribadi Anda, memperoleh izin untuk memodifikasi dan membahayakan sistem yang terhubung, seperti terminal titik penjualan dan sistem pemrosesan pesanan. Dalam beberapa kasus membajak seluruh jaringan komputer hingga biaya tebusan dikirimkan.")
        st.write("Terkadang peretas puas dengan mendapatkan data pribadi dan informasi kartu kredit Anda untuk keuntungan finansial. Dalam kasus lain, email phishing dikirim untuk mengumpulkan informasi login karyawan atau detail lainnya untuk digunakan dalam serangan yang lebih berbahaya terhadap beberapa individu atau perusahaan tertentu. Phishing adalah jenis serangan dunia maya yang harus dipelajari setiap orang untuk melindungi diri mereka sendiri dan memastikan keamanan email di seluruh organisasi")
        st.header("Bagaimana cara kerja phishing?")
        st.write("Phishing dimulai dengan email penipuan atau komunikasi lain yang dirancang untuk memikat korban. Pesan dibuat agar terlihat seolah-olah berasal dari pengirim terpercaya. Jika itu membodohi korban, korban dibujuk untuk memberikan informasi rahasia sering kali di situs web scam. Terkadang malware juga diunduh ke komputer target.")
        st.write("Penjahat dunia maya mulai dengan mengidentifikasi sekelompok individu yang ingin mereka targetkan. Kemudian mereka membuat email dan pesan teks yang tampak sah tetapi sebenarnya berisi tautan, lampiran, atau umpan berbahaya yang mengelabui target mereka agar mengambil tindakan yang tidak diketahui dan berisiko.")
        st.header("Jenis serangan phishing")
        st.subheader("1. Spear Phising")
        st.write("Spear phishing menargetkan individu tertentu, bukan sekelompok besar orang. Dengan begitu, penyerang dapat menyesuaikan komunikasi mereka dan tampil lebih otentik. Spear phishing sering kali merupakan langkah pertama yang digunakan untuk menembus pertahanan perusahaan dan melakukan serangan yang ditargetkan. Menurut SANS Institute, 95 persen dari semua serangan pada jaringan perusahaan adalah hasil dari spear phishing yang berhasil.")
        st.subheader("2. Microsoft 365 Phising ")
        st.write("Metode yang digunakan oleh penyerang untuk mendapatkan akses ke akun email Microsoft 365 cukup sederhana dan menjadi yang paling umum. Kampanye phishing ini biasanya berupa email palsu dari Microsoft. Email tersebut berisi permintaan untuk masuk, yang menyatakan bahwa pengguna perlu mengatur ulang kata sandi mereka, belum masuk baru-baru ini, atau bahwa ada masalah dengan akun yang perlu mereka perhatikan. URL disertakan, menarik pengguna untuk mengklik untuk mengatasi masalah tersebut")
        st.subheader("Business Email Compromise (BEC)")
        st.write("BEC secara hati-hati dalam merencanakan dan meneliti serangan yang menyamar sebagai vendor atau pemasok eksekutif perusahaan.")
        st.subheader("Whaling")
        st.write("Ketika penyerang mengejar ikan besar seperti CEO, itu disebut penangkapan ikan paus. Penyerang ini sering menghabiskan banyak waktu untuk membuat profil target untuk menemukan momen yang tepat dan cara untuk mencuri kredensial login. Penangkapan ikan paus menjadi perhatian khusus karena eksekutif tingkat tinggi dapat mengakses banyak informasi sensitif perusahaan.")
        st.subheader("Social Media Phish")
        st.write("Penyerang sering meneliti korban mereka di media sosial dan situs lain untuk mengumpulkan informasi terperinci, dan kemudian merencanakan serangan mereka dengan tepat.")
        st.subheader("Voice Phising")
        st.write("Phishing suara atau vishing , adalah bentuk rekayasa sosial. Ini adalah panggilan telepon palsu yang dirancang untuk mendapatkan informasi sensitif seperti kredensial login. Misalnya, penyerang mungkin menelepon berpura-pura menjadi agen pendukung atau perwakilan perusahaan Anda. Karyawan baru sering kali rentan terhadap jenis penipuan ini, tetapi hal itu dapat terjadi pada siapa saja dan menjadi lebih umum")
    
    if selected2==("10 Cara untuk menghindari phising"):
        st.header("10 Cara untuk menghindari phising")
        st.subheader("1. Tetap update tentang teknik phising")
        st.write("Penipuan phishing baru sedang dikembangkan setiap saat. Tanpa mengikuti teknik phishing baru ini, Anda dapat secara tidak sengaja menjadi mangsanya. Pantau terus berita tentang penipuan phishing baru. Dengan mencari tahu tentang mereka sedini mungkin, Anda akan memiliki risiko yang jauh lebih rendah untuk terjerat olehnya. Untuk administrator TI, pelatihan kesadaran keamanan berkelanjutan dan simulasi phishing untuk semua pengguna sangat disarankan untuk menjaga keamanan di seluruh organisasi. ")
        st.subheader("2. Berpikir dahulu sebelum klik!")
        st.write("Tidak apa-apa mengeklik tautan saat Anda berada di situs tepercaya. Mengklik tautan yang muncul di email acak dan pesan instan, bagaimanapun, bukanlah langkah yang cerdas. Arahkan kursor ke tautan yang Anda tidak yakin sebelum mengekliknya. Apakah mereka memimpin di mana mereka seharusnya memimpin? Email phishing mungkin mengklaim berasal dari perusahaan yang sah dan ketika Anda mengklik tautan ke situs web, itu mungkin terlihat persis seperti situs web sebenarnya. Email mungkin meminta Anda untuk mengisi informasi tetapi email tersebut mungkin tidak berisi nama Anda. Sebagian besar email phishing akan dimulai dengan 'Pelanggan yang Terhormat' sehingga Anda harus waspada saat menemukan email ini. Jika ragu, buka langsung sumbernya daripada mengklik tautan yang berpotensi berbahaya.")
        st.subheader("3. Instal Toolbar Anti-Phishing")
        st.write("Sebagian besar browser Internet populer dapat dikustomisasi dengan toolbar anti-phishing. Bilah alat tersebut menjalankan pemeriksaan cepat di situs yang Anda kunjungi dan membandingkannya dengan daftar situs phishing yang dikenal. Jika Anda menemukan situs berbahaya, bilah alat akan memberi tahu Anda tentang hal itu. Ini hanyalah satu lapisan perlindungan lagi terhadap penipuan phishing, dan ini sepenuhnya gratis. ")
        st.subheader("4. Verifikasi Keamanan Situs")
        st.write("Wajar jika Anda sedikit berhati-hati dalam memberikan informasi keuangan sensitif secara online. Namun, selama Anda berada di situs web yang aman, Anda tidak akan mengalami masalah apa pun. Sebelum mengirimkan informasi apa pun, pastikan URL situs dimulai dengan 'https' dan harus ada ikon kunci tertutup di dekat bilah alamat. Periksa juga sertifikat keamanan situs. Jika Anda mendapatkan pesan yang menyatakan bahwa situs web tertentu mungkin berisi file berbahaya, jangan buka situs web tersebut. Jangan pernah mengunduh file dari email atau situs web yang mencurigakan. Bahkan mesin pencari dapat menampilkan tautan tertentu yang dapat mengarahkan pengguna ke halaman web phishing yang menawarkan produk berbiaya rendah. Jika pengguna melakukan pembelian di situs web tersebut, detail kartu kredit akan diakses oleh penjahat dunia maya. ")
        st.subheader("5. Periksa Akun Online Anda Secara Teratur")
        st.write("Jika Anda tidak mengunjungi akun online untuk sementara waktu, seseorang mungkin sedang sibuk dengannya. Bahkan jika Anda secara teknis tidak perlu, periksa dengan setiap akun online Anda secara teratur. Biasakan juga mengganti kata sandi Anda secara teratur. Untuk mencegah phishing bank dan penipuan phishing kartu kredit, Anda harus secara pribadi memeriksa laporan Anda secara teratur. Dapatkan laporan bulanan untuk akun keuangan Anda dan periksa setiap entri dengan cermat untuk memastikan tidak ada transaksi penipuan yang dilakukan tanpa sepengetahuan Anda.")
        st.subheader("6. Perbarui Peramban Anda")
        st.write("Patch keamanan dirilis untuk peramban populer setiap saat. Mereka dirilis sebagai tanggapan terhadap celah keamanan yang pasti ditemukan dan dieksploitasi oleh phisher dan peretas lainnya. Jika Anda biasanya mengabaikan pesan tentang memperbarui browser Anda, berhentilah. Begitu pembaruan tersedia, unduh dan instal. ")
        st.subheader("7. Gunakan Firewall ")
        st.write("Firewall berkualitas tinggi bertindak sebagai penyangga antara Anda, komputer Anda, dan penyusup dari luar. Anda harus menggunakan dua jenis yang berbeda: firewall desktop dan firewall jaringan. Opsi pertama adalah jenis perangkat lunak, dan opsi kedua adalah jenis perangkat keras. Ketika digunakan bersama, mereka secara drastis mengurangi kemungkinan peretas dan phisher menyusup ke komputer atau jaringan Anda. ")
        st.subheader("8. Waspada Pop-Up ")
        st.write("Jendela pop-up sering menyamar sebagai komponen sah dari sebuah situs web. Namun, terlalu sering, itu adalah upaya phishing. Banyak browser populer memungkinkan Anda memblokir pop-up; Anda dapat mengizinkannya berdasarkan kasus per kasus. Jika seseorang berhasil lolos dari celah, jangan klik tombol 'batal' ; tombol seperti itu sering mengarah ke situs phishing. Sebagai gantinya, klik 'x' kecil di sudut atas jendela. ")
        st.subheader("9. Jangan Pernah Memberikan Informasi Pribadi")
        st.write("Sebagai aturan umum, Anda tidak boleh membagikan informasi pribadi atau yang sensitif secara finansial melalui Internet. Aturan ini mencakup semua jalan kembali ke hari-hari Amerika Online, ketika pengguna harus diperingatkan terus-menerus karena keberhasilan penipuan phishing awal. Jika ragu, kunjungi situs web utama perusahaan yang bersangkutan, dapatkan nomor mereka dan hubungi mereka. Sebagian besar email phishing akan mengarahkan Anda ke halaman di mana entri untuk informasi keuangan atau pribadi diperlukan. Pengguna Internet tidak boleh membuat entri rahasia melalui tautan yang disediakan dalam email. Jangan pernah mengirim email dengan informasi sensitif kepada siapa pun. Biasakan untuk memeriksa alamat situs web. Situs web yang aman selalu dimulai dengan ‘https’. ")
        st.subheader("10. Gunakan Perangkat Lunak Antivirus")
        st.write("Ada banyak alasan untuk menggunakan perangkat lunak antivirus. Tanda tangan khusus yang disertakan dengan perangkat lunak antivirus melindungi dari solusi dan celah teknologi yang diketahui. Pastikan untuk selalu memperbarui perangkat lunak Anda. Definisi baru ditambahkan setiap saat karena penipuan baru juga diimpikan setiap saat. Pengaturan anti-spyware dan firewall harus digunakan untuk mencegah serangan phishing dan pengguna harus memperbarui program secara teratur. Perlindungan firewall mencegah akses ke file berbahaya dengan memblokir serangan. Perangkat lunak antivirus memindai setiap file yang masuk melalui Internet ke komputer Anda. Ini membantu untuk mencegah kerusakan pada sistem Anda")

if selected==("Information"): 
    st.title("Halo, perkenalkan kami dari kelompok 8")
    st.write("Website ini berisi tentang cybersecurity dan phising. Masalah yang kami ambil adalah phising. Website ini berisi tentang edukasi tentang phising yang diharapka agar pengguna internet lebih berhati-hati dalam pemakaiannya.")
    st.write("Anggota Kelompok 8 :")
    st.write("1. Fahira Alhamid")
    st.write("2. Stefani Nadhea Hasanah")
    st.write("3. Annisa Nur Firdauzy")