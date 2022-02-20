from sqlalchemy import Column, Integer, String

from project.database import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dbn = Column(String(128), unique=False, nullable=True)
    school_name = Column(String(128), unique=False, nullable=True)
    category = Column(String(128), unique=False, nullable=True)
    year = Column(String(128), unique=False, nullable=True)
    total_enrollment = Column(String(128), unique=False, nullable=True)
    grade_k = Column(String(128), unique=False, nullable=True)
    grade_1 = Column(String(128), unique=False, nullable=True)
    grade_2 = Column(String(128), unique=False, nullable=True)
    grade_3 = Column(String(128), unique=False, nullable=True)
    grade_4 = Column(String(128), unique=False, nullable=True)
    grade_5 = Column(String(128), unique=False, nullable=True)
    grade_6 = Column(String(128), unique=False, nullable=True)
    grade_7 = Column(String(128), unique=False, nullable=True)
    grade_8 = Column(String(128), unique=False, nullable=True)
    female_1 = Column(String(128), unique=False, nullable=True)
    female_2 = Column(String(128), unique=False, nullable=True)
    male_1 = Column(String(128), unique=False, nullable=True)
    male_2 = Column(String(128), unique=False, nullable=True)
    asian_1 = Column(String(128), unique=False, nullable=True)
    asian_2 = Column(String(128), unique=False, nullable=True)
    black_1 = Column(String(128), unique=False, nullable=True)
    black_2 = Column(String(128), unique=False, nullable=True)
    hispanic_1 = Column(String(128), unique=False, nullable=True)
    hispanic_2 = Column(String(128), unique=False, nullable=True)
    other_1 = Column(String(128), unique=False, nullable=True)
    other_2 = Column(String(128), unique=False, nullable=True)
    white_1 = Column(String(128), unique=False, nullable=True)
    white_2 = Column(String(128), unique=False, nullable=True)
    ell_spanish_1 = Column(String(128), unique=False, nullable=True)
    ell_spanish_2 = Column(String(128), unique=False, nullable=True)
    ell_chinese_1 = Column(String(128), unique=False, nullable=True)
    ell_chinese_2 = Column(String(128), unique=False, nullable=True)
    ell_bengali_1 = Column(String(128), unique=False, nullable=True)
    ell_bengali_2 = Column(String(128), unique=False, nullable=True)
    ell_arabic_1 = Column(String(128), unique=False, nullable=True)
    ell_arabic_2 = Column(String(128), unique=False, nullable=True)
    ell_haitian_creole_1 = Column(String(128), unique=False, nullable=True)
    ell_haitian_creole_2 = Column(String(128), unique=False, nullable=True)
    ell_french_1 = Column(String(128), unique=False, nullable=True)
    ell_french_2 = Column(String(128), unique=False, nullable=True)
    ell_russian_1 = Column(String(128), unique=False, nullable=True)
    ell_russian_2 = Column(String(128), unique=False, nullable=True)
    ell_korean_1 = Column(String(128), unique=False, nullable=True)
    ell_korean_2 = Column(String(128), unique=False, nullable=True)
    ell_urdu_1 = Column(String(128), unique=False, nullable=True)
    ell_urdu_2 = Column(String(128), unique=False, nullable=True)
    ell_other_1 = Column(String(128), unique=False, nullable=True)
    ell_other_2 = Column(String(128), unique=False, nullable=True)
    ela_test_takers = Column(String(128), unique=False, nullable=True)
    ela_level_1_1 = Column(String(128), unique=False, nullable=True)
    ela_level_1_2 = Column(String(128), unique=False, nullable=True)
    ela_level_2_1 = Column(String(128), unique=False, nullable=True)
    ela_level_2_2 = Column(String(128), unique=False, nullable=True)
    ela_level_3_1 = Column(String(128), unique=False, nullable=True)
    ela_level_3_2 = Column(String(128), unique=False, nullable=True)
    ela_level_4_1 = Column(String(128), unique=False, nullable=True)
    ela_level_4_2 = Column(String(128), unique=False, nullable=True)
    ela_l3_l4_1 = Column(String(128), unique=False, nullable=True)
    ela_l3_l4_2 = Column(String(128), unique=False, nullable=True)
    math_test_takers = Column(String(128), unique=False, nullable=True)
    math_level_1_1 = Column(String(128), unique=False, nullable=True)
    math_level_1_2 = Column(String(128), unique=False, nullable=True)
    math_level_2_1 = Column(String(128), unique=False, nullable=True)
    math_level_2_2 = Column(String(128), unique=False, nullable=True)
    math_level_3_1 = Column(String(128), unique=False, nullable=True)
    math_level_3_2 = Column(String(128), unique=False, nullable=True)
    math_level_4_1 = Column(String(128), unique=False, nullable=True)
    math_level_4_2 = Column(String(128), unique=False, nullable=True)
    math_l3_l4_1 = Column(String(128), unique=False, nullable=True)
    math_l3_l4_2 = Column(String(128), unique=False, nullable=True)