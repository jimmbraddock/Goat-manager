CREATE SCHEMA `ferma` ;

create table ferma.gender (
  gender_id integer primary key not null,
  gender_name char not null
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;
insert into ferma.gender values (1, 'М');
insert into ferma.gender values (2, 'Ж');
commit;

CREATE TABLE ferma.breed (
    breed_id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    breed_name VARCHAR(128) NOT NULL
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;

CREATE TABLE ferma.goat (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    mother_id INTEGER,
    father_id INTEGER,
    gender_id INTEGER,
    date_of_birth DATE NOT NULL,
    breed_id INTEGER NOT NULL,
    birth_place VARCHAR(1024),
    CONSTRAINT `fk_goat_mother_id` FOREIGN KEY (`mother_id`)
        REFERENCES `goat` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_goat_father_id` FOREIGN KEY (`father_id`)
        REFERENCES `goat` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_goat_breed_id` FOREIGN KEY (`BREED_ID`)
        REFERENCES `breed` (`breed_ID`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_goat_gender_id` FOREIGN KEY (`gender_ID`)
        REFERENCES `gender` (`gender_ID`)
        ON DELETE CASCADE ON UPDATE CASCADE
)  ENGINE=INNODB DEFAULT CHARSET=UTF8;
  
