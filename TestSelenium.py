from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

class SeleniumTest:
    driver = webdriver.Chrome("C:\selenium75\chromedriver.exe")
    time_pause  = 6
    user_name = "vceballos"
    password ="1234"


    def user_include_selenium(self):
       try:
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_username_itemfield").send_keys("mguerrero")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_name_itemfield").send_keys(
            "manuel guerrero")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_email_itemfield").send_keys(
            "manuel.guerrero@gmail.com")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_password_itemfield").send_keys("1234")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_passwordConfirm_itemfield").send_keys(
            "1234")
        time.sleep(self.time_pause)
        Select(self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_languages_itemfield")).select_by_index('1')
        time.sleep(self.time_pause)
        checkboxSuper = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_usersEditGeneral_checkSuper_itemfield_control")
        checkboxSuper.click()
        time.sleep(self.time_pause)
        checkboxChat = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_usersEditGeneral_internalChatCheckbox_itemfield_control")
        checkboxChat.click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_usersEditGeneral_acceptButton_button").click()
       except NoSuchElementException as ex:
           print ex.message

    def user_delete_selenium(self):
       try:
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("manuel guerrero")
        time.sleep(self.time_pause)
        self.driver.find_element_by_class_name("remove").click()
        time.sleep(self.time_pause)
        btn_aceptar = self.driver.find_element_by_xpath(
            '/html/body/div[158]/div[2]/div/div[4]/div[2]/button[1]')
        btn_aceptar.click()
        time.sleep(self.time_pause)
       except NoSuchElementException as ex:
           print ex.message

    def user_update_selenium(self):
       try:
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("manuel guerrero")
        time.sleep(self.time_pause)
        self.driver.find_element_by_class_name("edit").click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_name_itemfield").clear()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_name_itemfield").send_keys(
            "Manuel Guerrero Narvaez ")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_email_itemfield").clear()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_email_itemfield").send_keys(
            "manuel.guerrero20@gmail.com")
        time.sleep(self.time_pause)
        Select(self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_languages_itemfield")).select_by_index('0')
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_labelChangePassword").click()
        time.sleep(self.time_pause)
        checkboxAgente = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_checkAgent_itemfield_control")
        checkboxAgente.click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_nrAgent_itemfield").send_keys(
            "1060")
        time.sleep(self.time_pause)
        checkboxCanales = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_checkTextAgent_itemfield_control3")
        checkboxCanales.click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_password_itemfield").send_keys(
            "1234")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_passwordConfirm_itemfield").send_keys(
            "1234")
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_profiles_perfilCheck_Administrador").click()
        time.sleep(self.time_pause)
        self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_moduleContent_accordion_edit_user_data_modifyButton_button").click()
       except NoSuchElementException as ex:
           print ex.message



    def extend_include_selenium(self):
       try:
         self.driver.find_element_by_css_selector(
        "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_departments_itemfield")).select_by_index('1')
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_extension_itemfield").send_keys("001200")
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_channel_type_itemfield")).select_by_index('1')
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_users_itemfield")).select_by_index('7')
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_key_itemfield").send_keys("1234")
         time.sleep(self.time_pause)
         checkboxEntrante = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_incoming_record_itemfield_control3")
         checkboxEntrante.click()
         time.sleep(self.time_pause)
         checkboxSaliente = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_outgoing_record_itemfield_control")
         checkboxSaliente.click()
         time.sleep(self.time_pause)
         checkbox_locales = self.driver.find_element_by_id(
             "main_moduleContent_current_view_active_module_local_record_itemfield_control")
         checkbox_locales.click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_acceptButton_button").click()
       except NoSuchElementException as ex:
           print ex.message
    def extend_update_selenium(self):
        try:
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
               "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("1200")
         time.sleep(self.time_pause)
         self.driver.find_element_by_class_name("edit").click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_key_itemfield").send_keys("1234")
         time.sleep(self.time_pause)
         checkboxEntrante = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_incoming_record_itemfield_control")
         checkboxEntrante.click()
         time.sleep(self.time_pause)
         checkboxSaliente = self.driver.find_element_by_id(
            "main_moduleContent_current_view_active_module_outgoing_record_itemfield_control")
         checkboxSaliente.click()
         time.sleep(self.time_pause)
         checkbox_locales = self.driver.find_element_by_id(
             "main_moduleContent_current_view_active_module_local_record_itemfield_control")
         checkbox_locales.click()
         time.sleep(self.time_pause)
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_departments_itemfield")).select_by_index('2')
         # Configuracion avanzada
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_labelConfig").click()
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_iaxConfig_typeAccount")).select_by_index('2')
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_iaxConfig_netMask").clear()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_iaxConfig_netMask").send_keys("120.1.60.32")
         time.sleep(self.time_pause)
         checkboxMonitor = self.driver.find_element_by_id(
             "main_moduleContent_current_view_active_module_iaxConfig_checkMonitorIAX_itemfield_control")
         checkboxMonitor.click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_modifyButton_button").click()
        except NoSuchElementException as ex:
            self.driver.execute_script("window.confirm = function(msg) { return true; }");
            print ex.message
    def extend_delete_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("1200")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name("remove").click()
            time.sleep(self.time_pause)
            btn_aceptar = self.driver.find_element_by_xpath(
                '/html/body/div[167]/div[2]/div/div[4]/div[2]/button[1]')
            btn_aceptar.click()
            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message


    def test_departament_selenium(self):
     try:
      self.driver.set_page_load_timeout(60)
      self.driver.get("http://canalesdigitales.expand/frontEnd/#login")
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#login_loginForm_user").send_keys("vceballos")
      self.driver.find_element_by_css_selector("#login_loginForm_password").send_keys("1234")
      self.driver.find_element_by_css_selector("#login_loginForm_password").send_keys(Keys.ENTER)
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicDepartments_link").click()
      time.sleep(self.time_pause)
      self.departament_include_selenium()
      self.departament_update_selenium()
      self.departament_delete_selenium()
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#main_moduleHeader_btnExit").click()
      time.sleep(4)
      self.driver.quit()
     except NoSuchElementException as ex:
       print ex.message


    def departament_include_selenium(self):
       try:
         self.driver.find_element_by_css_selector(
        "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_name_itemfield").send_keys("ventas")
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_description_itemfield").send_keys("Planes de venta")
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_acceptButton_button").click()
       except NoSuchElementException as ex:
           print ex.message

    def departament_update_selenium(self):
       try:
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
        "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("ventas")
         time.sleep(self.time_pause)
         self.driver.find_element_by_class_name("edit").click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_description_itemfield").clear()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_description_itemfield").send_keys("Planes de venta 12")
         time.sleep(self.time_pause)
         Select(self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_groups")).select_by_index('2')
         time.sleep(self.time_pause)
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_modifyButton_button").click()
       except NoSuchElementException as ex:
           print ex.message

    def departament_delete_selenium(self):
       try:
           time.sleep(self.time_pause)
           self.driver.find_element_by_css_selector(
               "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("ventas")
           time.sleep(self.time_pause)
           self.driver.find_element_by_class_name("remove").click()
           time.sleep(self.time_pause)
           btn_aceptar = self.driver.find_element_by_xpath(
               '/html/body/div[174]/div[2]/div/div[4]/div[2]/button[1]')
           btn_aceptar.click()
           time.sleep(self.time_pause)
       except NoSuchElementException as ex:
           print ex.message

    def tails_include_selenium(self):
        try:
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_name_itemfield").send_keys("Soporte")

            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_description_itemfield").send_keys("Soporte  Tecnico")

            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_types_itemfield")).select_by_index('1')
            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_departments_itemfield")).select_by_index('1')
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_checkInternal100").click()
            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_selectPriority100")).select_by_index('1')
            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_strategies_itemfield")).select_by_index('2')
            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_joinempty_itemfield")).select_by_index('1')
            time.sleep(self.time_pause)

            time.sleep(self.time_pause)
            Select(self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_leavewhenempty_itemfield")).select_by_index('1')
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_timeout_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_timeout_itemfield").send_keys("25")
            time.sleep(self.time_pause)

            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_retry_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_retry_itemfield").send_keys("2")
            time.sleep(self.time_pause)

            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_wrapuptime_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_wrapuptime_itemfield").send_keys("18")
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_queue_record_itemfield_control").click()


            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_acceptButton_button").click()
        except NoSuchElementException as ex:
            print ex.message

    def tails_update_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("Soporte")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name("edit").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_labelConfig").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_id(
                "main_moduleContent_current_view_active_module_advConfig_autofill_itemfield_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_id(
                "main_moduleContent_current_view_active_module_advConfig_timeoutrestart_itemfield_control").click()
            time.sleep(self.time_pause)
            time.sleep(self.time_pause)
            self.driver.find_element_by_id(
                "main_moduleContent_current_view_active_module_advConfig_autopause_itemfield_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_id(
                "main_moduleContent_current_view_active_module_advConfig_ringinuse_itemfield_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_weight_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_weight_itemfield").send_keys("2")
            time.sleep(self.time_pause)
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_maxlen_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_maxlen_itemfield").send_keys("2")
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_music_itemfield").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_advConfig_music_itemfield").send_keys("clasic")
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_modifyButton_button").click()
        except NoSuchElementException as ex:
            print ex.message

    def tails_delete_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("Soporte")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name("remove").click()
            time.sleep(self.time_pause)
            btn_aceptar = self.driver.find_element_by_xpath(
                '/html/body/div[183]/div[2]/div/div[4]/div[2]/button[1]')

            btn_aceptar.click()
            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message



    def profile_include_selenium(self):
       try:
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
        "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_generalDataContainer_name_itemfield").send_keys("supervisor")

         time.sleep(self.time_pause)
         accesscontrol = self.driver.find_element_by_css_selector(
            "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAlls_repeater_control_item_accesscontrol_desc_description")
         time.sleep(self.time_pause)
         tablescroll = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAssigned_dragContainerList > div > div.tablescroll_wrapper.ui-droppable")
         ActionChains(self.driver).drag_and_drop(accesscontrol, tablescroll).perform()
         time.sleep(self.time_pause)

         time.sleep(self.time_pause)
         bell = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAlls_repeater_control96_item_admin_name")
         time.sleep(self.time_pause)
         tablescroll = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAssigned_dragContainerList > div > div.tablescroll_wrapper.ui-droppable")
         ActionChains(self.driver).drag_and_drop(bell, tablescroll).perform()

         time.sleep(self.time_pause)
         chat = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAlls_repeater_control188_item_chat_desc_description")
         time.sleep(self.time_pause)
         tablescroll = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_resourcesAssigned_dragContainerList > div > div.tablescroll_wrapper.ui-droppable")
         ActionChains(self.driver).drag_and_drop( chat, tablescroll).perform()

         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalDataContainer_acceptButton_button").click()
       except Exception as ex:
           print ex.message

    def profile_update_selenium(self):
       try:
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
        "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("supervisor")
         time.sleep(self.time_pause)
         self.driver.find_element_by_class_name("edit").click()
         time.sleep(self.time_pause)

         time.sleep(self.time_pause)
         accesscontrol = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalData_resourcesAssigned_repeater_control_item_accesscontrol_desc_description")
         time.sleep(self.time_pause)
         tablescroll = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalData_resourcesAlls")
         ActionChains(self.driver).drag_and_drop(accesscontrol,tablescroll).perform()
         time.sleep(self.time_pause)
         tablescroll = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalData_resourcesAlls")
         time.sleep(self.time_pause)
         bell = self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalData_resourcesAssigned_repeater_control44_item_admin_desc_description")
         time.sleep(self.time_pause)
         ActionChains(self.driver).drag_and_drop(bell,tablescroll).perform()
         time.sleep(self.time_pause)
         self.driver.find_element_by_css_selector(
             "#main_moduleContent_current_view_active_module_generalData_modifyButton_button").click()
       except NoSuchElementException as ex:
           print ex.message

    def profile_delete_selenium(self):
       try:
           time.sleep(self.time_pause)
           self.driver.find_element_by_css_selector(
               "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("supervisor")
           time.sleep(self.time_pause)
           self.driver.find_element_by_class_name("remove").click()
           time.sleep(self.time_pause)
           btn_aceptar = self.driver.find_element_by_xpath(
               '/html/body/div[1522]/div[2]/div/div[4]/div[2]/button[1]')
           btn_aceptar.click()
           time.sleep(self.time_pause)
       except NoSuchElementException as ex:
           print ex.message

    def pauses_include_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_add_button").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_tablePauses_inputdtmf").send_keys(
                "30")
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_tablePauses_inputdescription").send_keys(
                " reunion planificacion")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name(
                "accept").click()
        except Exception as ex:
            print ex.message

    def pauses_update_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("30")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name("edit").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_tablePauses_inputdescription").clear()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_tablePauses_inputdescription").send_keys(
                "reunion planificacion 21")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name(
                "accept").click()
        except NoSuchElementException as ex:
            print ex.message

    def pauses_delete_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").clear()
            time.sleep(self.time_pause)
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector(
                "#main_moduleContent_current_view_active_module_toolbar_search_searchField").send_keys("30")
            time.sleep(self.time_pause)
            self.driver.find_element_by_class_name("remove").click()
            time.sleep(self.time_pause)
            btn_aceptar = self.driver.find_element_by_xpath(
                '/html/body/div[35]/div[2]/div/div[4]/div[2]/button[1]')
            btn_aceptar.click()
            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message

    def test_user_selenium(self):
     try:
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
      time.sleep(self.time_pause)
      self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicUsers_link").click()
      time.sleep(self.time_pause)
      self.user_include_selenium()
      self.user_update_selenium()
      self.user_delete_selenium()
      time.sleep(self.time_pause)
     except NoSuchElementException as ex:
       print ex.message

    def test_extend_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicExtensions_link").click()
            time.sleep(self.time_pause)
            self.extend_include_selenium()
            self.extend_update_selenium()
            self.extend_delete_selenium()
            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message

    def test_departament_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicDepartments_link").click()
            time.sleep(self.time_pause)
            self.departament_include_selenium()
            self.departament_update_selenium()
            self.departament_delete_selenium()
            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message

    def test_tails_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicQueues_link").click()
            time.sleep(self.time_pause)

            self.tails_include_selenium()
            self.tails_update_selenium()
            self.tails_delete_selenium()

            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message

    def test_profile_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicProfiles_link").click()
            time.sleep(self.time_pause)

            self.profile_include_selenium()
            self.profile_update_selenium()
            self.profile_delete_selenium()

            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
                print ex.message

    def test_pauses_selenium(self):
        try:
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftBar_categoryAdmin_control").click()
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#Web3\.LeftMenu_optBasicPauses_link").click()
            time.sleep(self.time_pause)

            test.pauses_include_selenium()
            test.pauses_update_selenium()
            test.pauses_delete_selenium()

            time.sleep(self.time_pause)
        except NoSuchElementException as ex:
            print ex.message


    def main_expand_selenium(self):
        try:
            self.driver.set_page_load_timeout(60)
            self.driver.get("http://canalesdigitales.expand/frontEnd/#login")
            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#login_loginForm_user").send_keys(self.user_name)
            self.driver.find_element_by_css_selector("#login_loginForm_password").send_keys(self.password)
            self.driver.find_element_by_css_selector("#login_loginForm_password").send_keys(Keys.ENTER)


            #test.test_user_selenium()
            #test.test_extend_selenium()
            #test.test_departament_selenium()
            #test.test_tails_selenium()
            #test.test_profile_selenium()
            test.test_pauses_selenium()

            time.sleep(self.time_pause)
            self.driver.find_element_by_css_selector("#main_moduleHeader_btnExit").click()
            time.sleep(4)
            self.driver.quit()
        except NoSuchElementException as ex:
            print ex.message


test = SeleniumTest()
test.main_expand_selenium()