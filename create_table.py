from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Inisialisasi database
Base = declarative_base()

# 3.5.1 Tabel Data Jaringan
class DataJaringan(Base):
    __tablename__ = 'data_jaringan'

    id_router = Column(Integer, primary_key=True, autoincrement=True)
    nama_router = Column(String(255), nullable=False)
    konfigurasi = Column(Text, nullable=False)
    data_lalu_lintas = Column(Text, nullable=True)
    data_log_ids = Column(Text, nullable=True)

# 3.5.2 Tabel Data Ancaman
class DataAncaman(Base):
    __tablename__ = 'data_ancaman'

    id_serangan = Column(Integer, primary_key=True, autoincrement=True)
    jenis_serangan = Column(String(255), nullable=False)
    deskripsi = Column(Text, nullable=False)
    tindakan = Column(Text, nullable=False)

# 3.5.3 Tabel Data Pengguna
class DataPengguna(Base):
    __tablename__ = 'data_pengguna'

    id_pengguna = Column(Integer, primary_key=True, autoincrement=True)
    nama_pengguna = Column(String(255), nullable=False)
    feedback = Column(Text, nullable=False)
    nilai_kepuasan = Column(Float, nullable=False)

# Konfigurasi database SQLite
engine = create_engine('sqlite:///data_penelitian.db')
Base.metadata.create_all(engine)

# Membuat sesi database
Session = sessionmaker(bind=engine)
session = Session()

# Menampilkan informasi sukses
print("Tabel-tabel telah berhasil dibuat di database.")
