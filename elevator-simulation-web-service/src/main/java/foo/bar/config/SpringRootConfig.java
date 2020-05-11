package foo.bar.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

/**
 * Created by jainpj on 18/02/17.
 */
@Configuration
@ComponentScan({ "foo.bar.service" })
public class SpringRootConfig {

}
