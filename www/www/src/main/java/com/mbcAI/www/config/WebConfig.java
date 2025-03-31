package com.mbcAI.www.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    // 웹소켓을 이용해서 파이썬의 imshow를 받아 처리함
    // 컨트롤러 대체용

    @Override
    public void addViewControllers(ViewControllerRegistry registry){

        registry.addViewController("/ai").setViewName("ai");
        // html 페이지를 직접 요청할 수 있도록 뷰-컨트롤러 설정 추가
    }   // http://localhost:8080/ai 요청시 ai.html이 오픈되게 설정함.
}
