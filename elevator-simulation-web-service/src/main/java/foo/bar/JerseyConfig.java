package foo.bar;

import org.glassfish.jersey.server.ResourceConfig;
import org.glassfish.jersey.servlet.ServletProperties;
import org.springframework.stereotype.Component;
import foo.bar.controllers.HackServiceController;
import foo.bar.controllers.PageLoadController;

/**
 * Created by jainpj on 18/02/17.
 */
@Component
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig() {

        registerEndpoints();

    }

    private void registerEndpoints() {

        register(PageLoadController.class);
        register(HackServiceController.class);
        property(ServletProperties.FILTER_FORWARD_ON_404,true);
    }
}
