from utils.tools import Point, Droite, Vecteur


class Vision:

    DISTANCE = 400

    def __init__(self, arene):
        self.elements = []
        self.arene = arene

    def sync_vision(self, robot):

        self.elements = []

        largeur = robot.WHEEL_BASE_WIDTH

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)
        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        vec_norme = Vecteur(a, b)
        left_droite = Droite.get_droite(vec_norme, a)
        right_droite = Droite.get_droite(vec_norme, b)

        for elem in self.arene.elements:

            seg = elem.segment
            new_vec_src = Vecteur(new_milieu, seg.src)
            new_vec_dest = Vecteur(new_milieu, seg.dest)

            if vec_norme.angle(new_vec_src) > 180 and vec_norme.angle(new_vec_dest) > 180:
                continue

            if seg.intersection(a, vec_src) is not None or seg.intersection(b, vec_src) is not None:
                seg_droite = seg.to_droite()

                if min(a.distance_to_droite(seg_droite), b.distance_to_droite(seg_droite)) > self.DISTANCE:
                    continue

                self.elements.append(elem)
                continue

            if max(seg.src.distance_to_droite(left_droite), seg.src.distance_to_droite(right_droite)) > largeur \
                    or max(seg.dest.distance_to_droite(left_droite), seg.dest.distance_to_droite(right_droite)) > largeur:
                continue

            self.elements.append(elem)

    def get_distance(self, robot):

        largeur = robot.WHEEL_BASE_WIDTH

        vec_norme = Vecteur(robot.chd, robot.cbd)
        vec_src = robot.vec_servo

        angle = vec_src.angle(vec_norme)
        milieu = robot.cbd

        if angle == 90:
            milieu = Point.milieu(robot.chd, robot.cbd)
        elif angle > 90:
            milieu = robot.chd

        a, b = Point.get_points_distance(milieu, vec_src, largeur//2)

        new_milieu = Droite.intersection(vec_src, Point.milieu(
            robot.chd, robot.cbd), Vecteur(a, b), a)
        if new_milieu == None:
            new_milieu = milieu
        else:
            a, b = Point.get_points_distance(new_milieu, vec_src, largeur//2)

        front_droite = Droite.get_droite(vec_src, new_milieu)

        mini = float("inf")
        for elem in self.elements:
            seg = elem.segment
            seg_droite = seg.to_droite()

            p1 = seg.intersection(a, vec_src)
            p2 = seg.intersection(b, vec_src)

            dist_inter_1 = float("inf")
            dist_inter_2 = float("inf")

            if p1 is not None or p2 is not None:

                if p1 is not None:
                    dist_inter_1 = p1.distance_to_droite(front_droite)

                if p2 is not None:
                    dist_inter_2 = p2.distance_to_droite(front_droite)

            dist_b = float("inf")
            dist_a = float("inf")

            if dist_inter_1 != float("inf") and dist_inter_2 != float("inf"):
                dist_a = a.distance_to_droite(seg_droite)
                dist_b = b.distance_to_droite(seg_droite)

            # Debug
            # print(">>>", "disp1", dist_inter_1, "distp2", dist_inter_2, "src", seg.src.distance_to_droite(front_droite), "dest", seg.dest.distance_to_droite(front_droite), "***", str(robot), "|||", seg_droite, "££", a, b, "--->", vec_src.vect, "dist a_b", dist_a, dist_b)

            mini = min(mini, dist_inter_1, dist_inter_2, seg.src.distance_to_droite(
                front_droite), seg.dest.distance_to_droite(front_droite), dist_a, dist_b)

        return mini

    def __str__(self):
        s = ""
        for elem in self.elements:
            s += str(elem) + ", "
        return s
