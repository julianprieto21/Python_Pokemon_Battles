from objects import Attack, Pokemon


disarming_voice = Attack("VOZ CAUTIVADORA", type=17, cat=1, power=40, acc=100, pp=15, stab=1)
metal_claw = Attack("GARRA METAL", type=16, cat=1, power=50, acc=95, pp=35, stab=1)
pursuit = Attack("PERSECUCION", type=15, cat=1, power=40, acc=100, pp=20, stab=1)
twister = Attack("CICLON", type=14, cat=1, power=40, acc=100,pp=20, stab=1)
astonish = Attack("IMPRESIONAR", type=13, cat=1, power=30, acc=100, pp=15, stab=1)
rollout = Attack("DESENRROLLAR", type=12, cat=1, power=30, acc=90, pp=20, stab=1)
silver_wind = Attack("VIENTO PLATA", type=11, cat=1, power=60, acc=100, pp=5, stab=1)
confusion = Attack("CONFUSION", type=10, cat=1, power=50, acc=100, pp=25, stab=1)
gust = Attack("TORNADO", type=9, cat=1, power=40, acc=100, pp=35, stab=1)
mud_lap = Attack("BOFETON LODO", type=8, cat=1, power=20, acc=100, pp=10, stab=1)
cross_poison = Attack("VENENO X", type=7, cat=1, power=70, acc=100, pp=20, stab=1)
force_palm = Attack("PALMEO", type=6, cat=1, power=60, acc=100, pp=10, stab=1)
powder_snow = Attack("NIEVE POLVO", type=5, cat=1, power=40, acc=100, pp=25, stab=1)
leafage = Attack("FOLLAJE", type=4, cat=1, power=40, acc=100 , pp=40, stab=1)
thunder_shock = Attack("IMPAC1NO", type=3, cat=1, power=40, acc=100, pp=30, stab=1)
water_gun = Attack("PISTOLA AGUA", type=2, cat=1, power=40, acc=100 ,pp=25, stab=1)
ember = Attack("ASCUAS", type=1, cat=1, power=40, acc=100, pp=25, stab=1)
scratch = Attack("ARAñAZO", type=0, cat=0, power=40, acc=100, pp=35, stab=0)

clefairy = Pokemon("CLEFAIRY", 17, (70, 45, 48, 60, 65, 35), [scratch, disarming_voice])
aron = Pokemon("ARON", 16, (50, 70, 100, 40, 40, 30), [scratch, metal_claw])
absol = Pokemon("ABSOL", 15, (65, 130, 60, 75, 60, 75), [scratch, pursuit])
datrini = Pokemon("DRATINI", 14, (41,64, 45, 50, 50, 50), [scratch, twister])
gastly = Pokemon("GASTLY", 13, (30, 35, 30, 100, 35, 80), [scratch, astonish])
geodude = Pokemon("GEODUDE", 12, (40, 80, 100, 30, 30 ,20), [scratch, rollout])
scypher = Pokemon("SCYPHER", 11, (70, 110, 80, 55, 80, 105), [scratch, silver_wind])
abra = Pokemon("ABRA", 10, (25, 20, 15, 105, 55, 90), [scratch, confusion])
pidgey = Pokemon("PIDGEY", 9, (40, 45, 40, 35, 35, 56), [scratch, gust])
cubone = Pokemon("CUBONE", 8, (50, 50, 95, 40, 50, 35), [scratch, mud_lap])
zubat = Pokemon("ZUBAT", 7, (40, 45, 35, 30, 40, 55), [scratch, cross_poison])
riolu = Pokemon("RIOLU", 6, (40, 70, 40, 35, 40, 60), [scratch, force_palm])
froslass = Pokemon("FROSLASS", 5, (70, 80, 70, 80, 70, 110), [scratch, powder_snow])
treecko = Pokemon("TREECKO", 4, (40, 45, 35, 65, 55, 70), [scratch, leafage])
shinx = Pokemon("SHINX", 3, (45, 65, 34, 40, 34, 45), [scratch, thunder_shock])
mudkip = Pokemon("MUDKIP", 2, (50, 70, 50, 50, 50, 40), [scratch, water_gun])
charmander = Pokemon("CHARMANDER", 1, (39, 52, 43, 60, 50, 65), [scratch, ember])

enemies =  [clefairy, aron, absol,
            datrini, gastly, geodude,
            scypher, abra, pidgey,
            cubone, zubat, riolu,
            froslass, treecko, shinx,
            mudkip, charmander]

fairy_wind = Attack("VIENTO FERRICO", type=17, cat=1, power=40, acc=100, pp=5, stab=1)
snarl = Attack("ALARIDO", type=15, cat=1, power=55, acc=95, pp=5, stab=1)
psybeam = Attack("PSICORRAYO", type=10, cat=1, power=65, acc=100, pp=5, stab=1)
icy_wind = Attack("VIENTO HIELO", type=5, cat=1, power=55, acc=95, pp=5, stab=1)
razor_leaf = Attack("HOJA AFILADA", type=4, cat=1, power=55, acc=95, pp=5, stab=1)
thunder_fang = Attack("COLMILLO TRUENO", type=3, cat=1, power=65, acc=95, pp=5, stab=1)
muddy_water = Attack("AGUA LODOSA", type=2, cat=1, power=90, acc=85, pp=5, stab=1)
lava_plume = Attack("HUMAREDA", type=1, cat=1, power=80, acc=100, pp=5, stab=1)

sylveon = Pokemon("SYLVEON", 17, (95, 65, 65, 110, 130, 60), [scratch, fairy_wind])
umbreon = Pokemon("UMBREON", 15, (95, 65, 110, 60, 130, 65), [scratch, snarl])
espeon = Pokemon("ESPEON", 10, (65, 65, 60, 130, 95, 110), [scratch, psybeam])
glaceon = Pokemon("GLACEON", 5, (65, 60, 110, 130, 95, 65), [scratch, icy_wind])
leafeon = Pokemon("LEAFEON", 4, (65, 110, 130, 60, 65, 95), [scratch, razor_leaf])
jolteon = Pokemon("JOLTEON", 3, (65, 65, 60, 110, 95, 130), [scratch, thunder_fang])
vaporeon = Pokemon("VAPOREON", 2, (130, 65, 60, 110, 95, 65), [scratch, muddy_water])
flareon = Pokemon("FLAREON", 1, (65, 130, 60, 95, 110, 65), [scratch, lava_plume ])

team = [sylveon, umbreon, 
        espeon, glaceon, 
        leafeon, jolteon,
        vaporeon, flareon]