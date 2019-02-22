# ############ A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
make_input = [[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # A4
              [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # A3
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # A6
              [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # R8
              [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # A8
              [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # A5
              [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # A7
              [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Pacific
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Civic
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # CRV
              [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Accord
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Fit
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # HRV
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Pilot
              [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Sportage
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Optima
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Forte
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Soul
              [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],  # Outlander
              [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Mirage
              [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Eclipse
              [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Lancer
              [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Range (Rover)
              [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],  # Discovery
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # X3
              [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Challenger
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],  # Journey
              [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Charger
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # Santa (Fe)
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],  # Tucson
              [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Elantra
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Ls
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # RX
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # IS
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # ES
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Altima
              [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Pathfinder
              [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Sentra
              [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Frontier
              [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],  # Versa
              [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # Rogue
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Armada
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],  # Camry
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Tacoma
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Land (cruiser)
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Corolla
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # 4Runner
              [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # CHR
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Fusion
              [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],  # Mustang
              [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Edge
              [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # Fiesta
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # Explorer
              [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Escape
              [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # Focus
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],  # QX50
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],  # QX60
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0],  # QX30
              [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],  # QX80
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],  # QX70
              [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # CX 5
              [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # CX 7
              [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # CX 9
              [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Cherokee
              [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Compass
              [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # Wrangler
              [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # RenegaDe (Cherokee)
              [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Grand
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]]  # Other
# ############ A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z

# ############## A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
damage_input = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # All Over
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # Burn
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Hail
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Partial
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # Stripped
                [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],  # Water
                [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Biohazardous
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Mechanical
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Rear
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # Top/Roof
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Frame
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Minor
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],  # Rollover
                [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],  # Undercarriage
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Front
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Normal
                [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Side
                [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]]  # Vandalism

                    # Y__N
make_output = [[0],  # 1
               [0],  # 2
               [0],  # 3
               [0],  # 4
               [0],  # 5
               [0],  # 6
               [0],  # 7
               [0],  # 8
               [0],  # 9
               [0],  # 10
               [0],  # 11
               [0],  # 12
               [1],  # 13
               [0],  # 14
               [1],  # 15
               [1],  # 16
               [1],  # 17
               [0],  # 18
               [0],  # 19
               [0],  # 20
               [0],  # 21
               [0],  # 22
               [0],  # 23
               [1],  # 24
               [0],  # 25
               [0],  # 26
               [0],  # 27
               [0],  # 28
               [0],  # 29
               [0],  # 30
               [0],  # 31
               [0],  # 32
               [0],  # 33
               [0],  # 34
               [0],  # 35
               [0],  # 36
               [0],  # 37
               [0],  # 38
               [0],  # 39
               [0],  # 40
               [0],  # 41
               [0],  # 42
               [0],  # 43
               [0],  # 44
               [0],  # 45
               [0],  # 46
               [0],  # 47
               [0],  # 48
               [1],  # 49
               [0],  # 50
               [0],  # 51
               [0],  # 52
               [1],  # 53
               [0],  # 54
               [1],  # 54
               [0],  # 55
               [0],  # 56
               [0],  # 57
               [0],  # 58
               [0],  # 59
               [1],  # 60
               [0],  # 61
               [0],  # 62
               [0],  # 63
               [0],  # 64
               [0],  # 65
               [0],  # 66
               [1],  # 67
               [1],  # 68
               [0],  # 69
               [0],  # 70
               [0],  # 71
               [0],  # 72
               [0],  # 73
               [0],  # 74
               [0],  # 75
               [0],  # 76
               [1],  # 77
               [0],  # 78
               [0],  # 79
               [0],  # 80
               [0],  # 81
               [0],  # 82
               [0],  # 83
               [0],  # 84
               [0],  # 85
               [1],  # 86
               [1],  # 87
               [1],  # 88
               [0],  # 89
               [1],  # 90
               [0],  # 91
               [0],  # 92
               [0],  # 93
               [0]]  # 94


class Neuron():

    def __init__(self, num):
        self.weight_list = []
        self.value_list = []
        self.num_inputs = num
        self.sum = 0
        self.output = 0

        for i in range(0, self.num_inputs - 1):
            self.weight_list.append(random.uniform(-0.1, 0.1))
            self.value_list.append(0)

        # Bias
        self.weight_list.append(random.uniform(-0.1, 0.1))
        self.value_list.append(1)

    def calculate(self):
        self.sum = 0
        for i in range(0, self.num_inputs):
            self.sum += self.weight_list[i] * self.value_list[i]
        self.output = sigmoid(self.sum)


def sigmoid(x):

    ans = 1 / (1 + (2.718 ** (-x)))
    return ans


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


input_layer = [Neuron(1) for i in range(0, 26)]
hidden_layer1 = [Neuron(27) for i in range(0, 128)]
hidden_layer2 = [Neuron(129) for i in range(0, 32)]
output_layer = [Neuron(33)]

input_error = []
hidden1_error = []
hidden2_error = []
output_error = []

for x in range(0, len(input_layer)):
    input_error.append(0)
for x in range(0, len(hidden_layer1)):
    hidden1_error.append(0)
for x in range(0, len(hidden_layer2)):
    hidden2_error.append(0)
for x in range(0, len(output_layer)):
    output_error.append(0)

error_matrix = [input_error, hidden1_error, hidden2_error, output_error]
network = [input_layer, hidden_layer1, hidden_layer2, output_layer]


def print_layer(layer):
    for i in range(0, len(layer)):
        print("Node " + str(i) + "'s output was: " + str(layer[i].output))


def forward_propagation(test_case):

    # Set inputs for the first hidden layer
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer)):
            hidden_layer1[x].value_list[y] = make_input[test_case][y]
    # Calculate
    for i in range(0, len(hidden_layer1)):
        hidden_layer1[i].calculate()

    # Set inputs for the second hidden layer
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1)):
            hidden_layer2[x].value_list[y] = hidden_layer1[y].output
    # Calculate
    for i in range(0, len(hidden_layer2)):
        hidden_layer2[i].calculate()

    # Set inputs for the output layer
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].value_list[y] = hidden_layer2[y].output
    # Calculate
    for i in range(0, len(output_layer)):
        output_layer[x].calculate()


def backward_propagation(test_case, learning_rate):

    # Calculate error for output layer
    for x in range(0, len(output_layer)):
        output_error[x] = sigmoid_prime(output_layer[x].sum) * (make_output[test_case][x] - output_layer[x].output)

    # Calculate error for second hidden layer
    for x in range(0, len(hidden_layer2)):
        temp = 0
        for y in range(0, len(output_layer)):
            temp += output_layer[y].weight_list[x] * output_error[y]
        hidden2_error[x] = sigmoid_prime(hidden_layer2[x].sum) * temp

    # Calculate error for first hidden layer
    for x in range(0, len(hidden_layer1)):
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += hidden_layer2[y].weight_list[x] * hidden2_error[y]
        hidden1_error[x] = sigmoid_prime(hidden_layer1[x].sum) * temp

    # Assign new weights to output layer
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2) + 1):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (learning_rate *
                    output_layer[x].value_list[y] * output_error[x])

    # Assign new weights to second layer
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1) + 1):
            hidden_layer2[x].weight_list[y] = hidden_layer2[x].weight_list[y] + (learning_rate *
                    hidden_layer2[x].value_list[y] * hidden2_error[x])

    # Assign new weights to first layer
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer) + 1):
            hidden_layer1[x].weight_list[y] = hidden_layer1[x].weight_list[y] + (learning_rate *
                    hidden_layer1[x].value_list[y] * hidden1_error[x])


def train():
    iterations = 0
    learning_rate = 0.5

    print()
    while iterations < 500:
        test_case = 0

        print(len(output_layer))
        while test_case < 26:
            forward_propagation(test_case)
            backward_propagation(test_case, learning_rate)
            print(str(output_layer[0].output) + " " + str(test_case))
            test_case += 1

        iterations += 1


train()
