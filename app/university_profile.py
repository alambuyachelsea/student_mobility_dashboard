class University:
    def __init__(self, name, qs_ranking, monthly_expenses,
                 summer_temp_ave, winter_temp_ave, social_activity_level,
                 country, visa_assistance, sustainability_score,
                 gym_amenities, safety_rating, language_support):
    
        self._name = name
        self._qs_ranking = qs_ranking
        self._monthly_expenses = monthly_expenses
        self._summer_temp_ave = summer_temp_ave
        self._winter_temp_ave = winter_temp_ave
        self._social_activity_level = social_activity_level
        self._country = country
        self._visa_assistance = visa_assistance
        self._sustainability_score = sustainability_score
        self._gym_amenities = gym_amenities
        self._safety_rating = safety_rating
        self._language_support = language_support

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def qs_ranking(self):
        return self._qs_ranking

    @property
    def monthly_expenses(self):
        return self._monthly_expenses

    @property
    def summer_temp_ave(self):
        return self._summer_temp_ave

    @property
    def winter_temp_ave(self):
        return self._winter_temp_ave

    @property
    def social_activity_level(self):
        return self._social_activity_level

    @property
    def country(self):
        return self._country

    @property
    def visa_assistance(self):
        return self._visa_assistance

    @property
    def sustainability_score(self):
        return self._sustainability_score

    @property
    def gym_amenities(self):
        return self._gym_amenities

    @property
    def safety_rating(self):
        return self._safety_rating

    @property
    def language_support(self):
        return self._language_support

    # Setters
    @name.setter
    def name(self, value):
        self._name = value

    @qs_ranking.setter
    def qs_ranking(self, value):
        self._qs_ranking = value

    @monthly_expenses.setter
    def monthly_expenses(self, value):
        self._monthly_expenses = value

    @summer_temp_ave.setter
    def summer_temp_ave(self, value):
        self._summer_temp_ave = value

    @winter_temp_ave.setter
    def winter_temp_ave(self, value):
        self._winter_temp_ave = value

    @social_activity_level.setter
    def social_activity_level(self, value):
        self._social_activity_level = value

    @country.setter
    def country(self, value):
        self._country = value

    @visa_assistance.setter
    def visa_assistance(self, value):
        self._visa_assistance = value

    @sustainability_score.setter
    def sustainability_score(self, value):
        self._sustainability_score = value

    @gym_amenities.setter
    def gym_amenities(self, value):
        self._gym_amenities = value

    @safety_rating.setter
    def safety_rating(self, value):
        self._safety_rating = value

    @language_support.setter
    def language_support(self, value):
        self._language_support = value

    def __repr__(self):
        return (f"University(name={self.name}, qs_ranking={self.qs_ranking}, monthly_expenses={self.monthly_expenses}, "
                f"summer_temp_ave={self.summer_temp_ave}, winter_temp_ave={self.winter_temp_ave}, "
                f"social_activity_level={self.social_activity_level}, country={self.country}, visa_assistance={self.visa_assistance}, "
                f"sustainability_score={self.sustainability_score}, gym_amenities={self.gym_amenities}, safety_rating={self.safety_rating}, "
                f"language_support={self.language_support})")
