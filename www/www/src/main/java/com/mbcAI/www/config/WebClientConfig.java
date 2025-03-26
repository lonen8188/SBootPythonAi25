package com.mbcAI.www.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.ExchangeStrategies;
import org.springframework.web.reactive.function.client.WebClient;

@Configuration
public class WebClientConfig {
    // 이미지를 보내든 영상을 보내든 데이터의 용량이 크기 때문에 버퍼 사이즈 조절해야 한다.

    // Webclient를 구성하고 빈으로 정의하여 애플리케이션에서 사용할 수 있도록 함

    @Bean
    WebClient webClient() {
        return WebClient.builder().exchangeStrategies(ExchangeStrategies.builder()
                        .codecs(configurer
                                -> configurer.defaultCodecs().maxInMemorySize(-1)) //무제한 버퍼
                        .build())
                .baseUrl("http://localhost:8000")   // 업로드한 파일을 ai 서버에 전송하기 위해서 버퍼의 크기 제한을 제한 없이
                .build();  //https://m.blog.naver.com/seek316/223337685249
    }
}
